from collections import namedtuple

from fetching import FetchError
from temperature import feels_like, to_celsius

Query = namedtuple('Query', ['kind', 'scale', 'length', 'limit'])

_TEMPERATURE_KINDS = ('AIR', 'FEELS')
_PERCENT_KINDS = ('HUMIDITY', 'PRECIPITATION')


def parse_query(line: str) -> Query:
    parts = line.split()
    if parts[0] == 'TEMPERATURE':
        return Query(parts[1], parts[2], int(parts[3]), parts[4])
    return Query(parts[0], None, int(parts[1]), parts[2])


def answer(forecast, query: Query) -> str:
    """Returns the query's result as a "date time value" line of output."""
    best_value = None
    best_period = None

    for period in forecast.periods[: query.length]:
        value = _value(period, query)
        if value is None:
            continue
        better = best_value is None
        if not better:
            better = value > best_value if query.limit == 'MAX' else value < best_value
        if better:
            best_value = value
            best_period = period

    if best_period is None:
        raise FetchError('FORMAT', forecast.source)

    suffix = '%' if query.kind in _PERCENT_KINDS else ''
    return f'{_iso(best_period.start)} {best_value:.4f}{suffix}'


def _value(period, query: Query):
    if query.kind == 'AIR':
        temperature = period.temperature
    elif query.kind == 'FEELS':
        if period.humidity is None or period.wind is None:
            return None
        temperature = feels_like(period.temperature, period.humidity, period.wind)
    elif query.kind == 'HUMIDITY':
        return period.humidity
    elif query.kind == 'WIND':
        return period.wind
    else:
        return period.precipitation

    return to_celsius(temperature) if query.scale == 'C' else temperature


def _iso(start) -> str:
    return start.strftime('%Y-%m-%dT%H:%M:%SZ')
