from collections import namedtuple

Location = namedtuple('Location', ['latitude', 'longitude'])


def format_location(location: Location) -> str:
    """Returns a location in the "33.64324045/N 117.84185686276017/W" format."""
    latitude, longitude = location
    latitude_letter = 'N' if latitude >= 0 else 'S'
    longitude_letter = 'E' if longitude >= 0 else 'W'
    return f'{abs(latitude)}/{latitude_letter} {abs(longitude)}/{longitude_letter}'
