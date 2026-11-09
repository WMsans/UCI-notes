import unittest

from location import Location, format_location
from queries import Query, answer, parse_query
from temperature import feels_like, to_celsius, to_fahrenheit
from weather import Period


class TestTemperature(unittest.TestCase):
    def test_conversions(self):
        self.assertAlmostEqual(to_celsius(32), 0)
        self.assertAlmostEqual(to_celsius(212), 100)
        self.assertAlmostEqual(to_celsius(73), 22.77777777777778)
        self.assertAlmostEqual(to_fahrenheit(0), 32)
        self.assertAlmostEqual(to_fahrenheit(100), 212)
        self.assertAlmostEqual(to_fahrenheit(to_celsius(73)), 73)


class TestFeelsLike(unittest.TestCase):
    def test_heat_index_at_and_above_68(self):
        self.assertAlmostEqual(feels_like(95, 55, 0), 108.94701570000005)
        self.assertAlmostEqual(feels_like(68, 50, 10), 77.35084221999998)

    def test_wind_chill_at_and_below_50(self):
        self.assertAlmostEqual(feels_like(20, 50, 10), 8.854038235710776)
        self.assertAlmostEqual(feels_like(50, 50, 4), 48.87024835953933)

    def test_wind_chill_needs_wind_over_three(self):
        self.assertEqual(feels_like(50, 50, 3), 50)
        self.assertEqual(feels_like(20, 50, 3), 20)

    def test_between_50_and_68_is_air_temperature(self):
        self.assertEqual(feels_like(60, 90, 20), 60)
        self.assertEqual(feels_like(67.9, 10, 100), 67.9)


class TestLocation(unittest.TestCase):
    def test_north_and_west(self):
        self.assertEqual(
            format_location(Location(33.64324045, -117.84185686276017)),
            '33.64324045/N 117.84185686276017/W',
        )

    def test_south_and_east(self):
        self.assertEqual(
            format_location(Location(-33.5, 151.25)), '33.5/S 151.25/E'
        )


class TestQueries(unittest.TestCase):
    def setUp(self):
        from datetime import datetime, timezone

        def period(hour, temperature, humidity=10, wind=5, precipitation=0):
            return Period(
                datetime(2024, 1, 1, hour, tzinfo=timezone.utc),
                temperature,
                humidity,
                wind,
                precipitation,
            )

        # Hours 0, 1, and 2; the first and last share the maximum temperature.
        self.forecast = type(
            'Forecast',
            (),
            {
                'periods': [period(0, 70), period(1, 50), period(2, 70)],
                'source': 'test',
            },
        )()

    def test_parses_every_query_form(self):
        self.assertEqual(
            parse_query('TEMPERATURE FEELS C 12 MIN'), Query('FEELS', 'C', 12, 'MIN')
        )
        self.assertEqual(parse_query('HUMIDITY 24 MAX'), Query('HUMIDITY', None, 24, 'MAX'))

    def test_ties_report_the_earliest_hour(self):
        self.assertEqual(
            answer(self.forecast, Query('AIR', 'F', 3, 'MAX')),
            '2024-01-01T00:00:00Z 70.0000',
        )
        self.assertEqual(
            answer(self.forecast, Query('AIR', 'F', 3, 'MIN')),
            '2024-01-01T01:00:00Z 50.0000',
        )

    def test_converts_temperature_and_marks_percentages(self):
        self.assertEqual(
            answer(self.forecast, Query('AIR', 'C', 1, 'MAX')),
            '2024-01-01T00:00:00Z 21.1111',
        )
        self.assertEqual(
            answer(self.forecast, Query('HUMIDITY', None, 1, 'MIN')),
            '2024-01-01T00:00:00Z 10.0000%',
        )
        self.assertEqual(
            answer(self.forecast, Query('WIND', None, 1, 'MAX')),
            '2024-01-01T00:00:00Z 5.0000',
        )

    def test_length_beyond_available_hours_uses_what_is_there(self):
        self.assertEqual(
            answer(self.forecast, Query('AIR', 'F', 100, 'MAX')),
            '2024-01-01T00:00:00Z 70.0000',
        )
