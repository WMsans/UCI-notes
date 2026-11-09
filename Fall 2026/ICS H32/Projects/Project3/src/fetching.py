import json
import urllib.error
import urllib.request

USER_AGENT = '(https://ics.uci.edu/~thornton/icsh32/ProjectGuide/Project3/, jeremyz4@uci.edu)'

class FetchError(Exception):
    """Failure whose code and source become the FAILED line of output."""

    def __init__(self, code: str, source: str, status: int | None = None) -> None:
        super().__init__(f'{code}: {source}')
        self.code = code
        self.status = status
        self.source = source if status is None else f'{status} {source}'


def fetch_json(url: str, accept: str = 'application/json'):
    """JSON from a URL. Every way it can go wrong comes back as FetchError."""
    request = urllib.request.Request(
        url, headers={'User-Agent': USER_AGENT, 'Accept': accept}
    )

    try:
        with urllib.request.urlopen(request) as response:
            status = response.status
            body = response.read()
    except urllib.error.HTTPError as error:
        raise FetchError('NOT 200', url, error.code) from error
    except (urllib.error.URLError, OSError) as error:
        raise FetchError('NETWORK', url) from error

    if status != 200:
        raise FetchError('NOT 200', url, status)

    try:
        return json.loads(body)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise FetchError('FORMAT', url, status) from error


def read_json(path: str):
    """Same as fetch_json, but from a file that was saved earlier."""
    try:
        with open(path, encoding='utf-8') as file:
            body = file.read()
    except OSError as error:
        raise FetchError('MISSING', path) from error

    try:
        return json.loads(body)
    except json.JSONDecodeError as error:
        raise FetchError('FORMAT', path) from error
