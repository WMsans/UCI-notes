import time
import urllib.parse

from fetching import FetchError, fetch_json, read_json
from location import Location

_SEARCH_URL = 'https://nominatim.openstreetmap.org/search'
_REVERSE_URL = 'https://nominatim.openstreetmap.org/reverse'

_last_request = 0.0


def _nominatim_json(url: str):
    """Fetches JSON from Nominatim, never sending requests less than a second apart."""
    global _last_request
    wait = _last_request + 1.0 - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last_request = time.monotonic()
    return fetch_json(url)


def _location_from(raw, source: str, status: int | None = None) -> Location:
    """Pulls a latitude and longitude out of one Nominatim result."""
    try:
        return Location(float(raw['lat']), float(raw['lon']))
    except (KeyError, TypeError, ValueError) as error:
        raise FetchError('FORMAT', source, status) from error


def _description_from(raw, source: str, status: int | None = None) -> str:
    """Pulls the address out of one Nominatim reverse geocoding result."""
    description = raw.get('display_name') if isinstance(raw, dict) else None
    if not isinstance(description, str):
        raise FetchError('FORMAT', source, status)
    return description


class ForwardFile:
    """Forward geocodes a location using a file of saved Nominatim results."""

    def __init__(self, path: str) -> None:
        self._path = path

    def location(self) -> Location:
        results = read_json(self._path)
        if not isinstance(results, list) or not results:
            raise FetchError('FORMAT', self._path)
        return _location_from(results[0], self._path)


class ForwardNominatim:
    """Forward geocodes a location by asking Nominatim's API."""

    def __init__(self, query: str) -> None:
        self._query = query

    def location(self) -> Location:
        url = f'{_SEARCH_URL}?' + urllib.parse.urlencode(
            {'q': self._query, 'format': 'jsonv2', 'limit': 1}
        )
        results = _nominatim_json(url)
        if not isinstance(results, list) or not results:
            raise FetchError('FORMAT', url, 200)
        return _location_from(results[0], url, 200)


class ReverseFile:
    """Reverse geocodes a location using a file of saved Nominatim results."""

    def __init__(self, path: str) -> None:
        self._path = path

    def describe(self, location: Location) -> str:
        return _description_from(read_json(self._path), self._path)


class ReverseNominatim:
    """Reverse geocodes a location by asking Nominatim's API."""

    def describe(self, location: Location) -> str:
        url = f'{_REVERSE_URL}?' + urllib.parse.urlencode(
            {'lat': location.latitude, 'lon': location.longitude, 'format': 'jsonv2'}
        )
        return _description_from(_nominatim_json(url), url, 200)
