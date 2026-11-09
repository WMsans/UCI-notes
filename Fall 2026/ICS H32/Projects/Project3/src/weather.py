import re
from collections import namedtuple
from datetime import datetime, timezone

from fetching import FetchError, fetch_json, read_json
from location import Location
from temperature import to_fahrenheit

_GEO_JSON = 'application/geo+json'
_POINTS_URL = 'https://api.weather.gov/points/'
_NUMBER = re.compile(r'-?\d+(?:\.\d+)?')

# temperature is always in Fahrenheit
Period = namedtuple(
    'Period', ['start', 'temperature', 'humidity', 'wind', 'precipitation']
)
HourlyForecast = namedtuple('HourlyForecast', ['location', 'periods', 'source'])


class WeatherFile:
    """Hourly forecast from a saved NWS response."""

    def __init__(self, path: str) -> None:
        self._path = path

    def hourly(self, latitude: float, longitude: float) -> HourlyForecast:
        return _forecast(read_json(self._path), self._path)


class WeatherNws:
    """Hourly forecast from the live API: two calls, points then forecast."""

    def hourly(self, latitude: float, longitude: float) -> HourlyForecast:
        points_url = f'{_POINTS_URL}{latitude},{longitude}'
        points = fetch_json(points_url, _GEO_JSON)
        try:
            forecast_url = points['properties']['forecastHourly']
        except (KeyError, TypeError) as error:
            raise FetchError('FORMAT', points_url, 200) from error
        if not isinstance(forecast_url, str):
            raise FetchError('FORMAT', points_url, 200)
        return _forecast(fetch_json(forecast_url, _GEO_JSON), forecast_url, 200)


def _mean(values) -> float:
    values = list(values)
    total = 0.0
    for value in values:
        total += value
    return total / len(values)


def _number(value) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return value


def _quantity(raw) -> float | None:
    return _number(raw.get('value')) if isinstance(raw, dict) else None


def _forecast(raw, source: str, status: int | None = None) -> HourlyForecast:
    try:
        coordinates = raw['geometry']['coordinates'][0]
        periods = raw['properties']['periods']
    except (KeyError, IndexError, TypeError) as error:
        raise FetchError('FORMAT', source, status) from error

    if not isinstance(coordinates, list) or not isinstance(periods, list):
        raise FetchError('FORMAT', source, status)

    points = []
    for point in coordinates:
        try:
            points.append((float(point[1]), float(point[0])))
        except (IndexError, TypeError, ValueError) as error:
            raise FetchError('FORMAT', source, status) from error
    if not points:
        raise FetchError('FORMAT', source, status)

    # The same point is often reported more than once, so average the unique ones.
    unique = list(dict.fromkeys(points))
    location = Location(
        _mean(latitude for latitude, _ in unique),
        _mean(longitude for _, longitude in unique),
    )

    return HourlyForecast(location, [_period(p, source, status) for p in periods], source)


def _period(raw, source: str, status: int | None = None) -> Period:
    try:
        start = datetime.fromisoformat(raw['startTime']).astimezone(timezone.utc)
        temperature = _number(raw['temperature'])
    except (KeyError, TypeError, ValueError, AttributeError) as error:
        raise FetchError('FORMAT', source, status) from error
    if temperature is None:
        raise FetchError('FORMAT', source, status)

    if raw.get('temperatureUnit') == 'C':
        temperature = to_fahrenheit(temperature)

    wind = raw.get('windSpeed')
    match = _NUMBER.search(wind) if isinstance(wind, str) else None

    return Period(
        start,
        temperature,
        _quantity(raw.get('relativeHumidity')),
        float(match.group()) if match else None,
        _quantity(raw.get('probabilityOfPrecipitation')),
    )
