import sys

from fetching import FetchError
from geocoding import ForwardFile, ForwardNominatim, ReverseFile, ReverseNominatim
from location import format_location
from queries import answer, parse_query
from weather import WeatherFile, WeatherNws

_FORWARD_ATTRIBUTION = '**Forward geocoding data from OpenStreetMap'
_REVERSE_ATTRIBUTION = '**Reverse geocoding data from OpenStreetMap'
_WEATHER_ATTRIBUTION = (
    '**Real-time weather data from National Weather Service, '
    'United States Department of Commerce'
)


def main() -> None:
    print('\n'.join(process(sys.stdin.read().splitlines())))


def process(lines) -> list[str]:
    """Returns the lines of output for the given lines of input."""
    try:
        return _process(lines)
    except FetchError as error:
        return ['FAILED', error.source, error.code]


def _process(lines) -> list[str]:
    lines = iter(lines)

    _, target_kind, target_argument = _split(next(lines))
    if target_kind == 'NOMINATIM':
        forward = ForwardNominatim(target_argument)
    else:
        forward = ForwardFile(target_argument)

    _, weather_kind, weather_argument = _split(next(lines))
    if weather_kind == 'NWS':
        weather = WeatherNws()
    else:
        weather = WeatherFile(weather_argument)

    queries = []
    for line in lines:
        if line.strip() == 'NO MORE QUERIES':
            break
        queries.append(parse_query(line))

    _, reverse_kind, reverse_argument = _split(next(lines))
    if reverse_kind == 'NOMINATIM':
        reverse = ReverseNominatim()
    else:
        reverse = ReverseFile(reverse_argument)

    target = forward.location()
    forecast = weather.hourly(target.latitude, target.longitude)
    description = reverse.describe(forecast.location)

    output = [
        f'TARGET {format_location(target)}',
        f'FORECAST {format_location(forecast.location)}',
        description,
    ]
    output += [answer(forecast, query) for query in queries]

    if target_kind == 'NOMINATIM':
        output.append(_FORWARD_ATTRIBUTION)
    if reverse_kind == 'NOMINATIM':
        output.append(_REVERSE_ATTRIBUTION)
    if weather_kind == 'NWS':
        output.append(_WEATHER_ATTRIBUTION)

    return output


def _split(line: str) -> list[str]:
    """Splits an input line into its keyword, its kind, and the rest of the line."""
    parts = [part.strip() for part in line.split(maxsplit=2)]
    return parts + [''] * (3 - len(parts))


if __name__ == '__main__':
    main()
