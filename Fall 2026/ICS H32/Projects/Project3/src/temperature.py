def to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def feels_like(fahrenheit: float, humidity: float, wind_mph: float) -> float:
    """Returns the "feels like" temperature, in degrees Fahrenheit."""
    if fahrenheit >= 68:
        t = fahrenheit
        h = humidity
        return (
            -42.379
            + 2.04901523 * t
            + 10.14333127 * h
            - 0.22475541 * t * h
            - 0.00683783 * t**2
            - 0.05481717 * h**2
            + 0.00122874 * t**2 * h
            + 0.00085282 * t * h**2
            - 0.00000199 * t**2 * h**2
        )

    if fahrenheit <= 50 and wind_mph > 3:
        t = fahrenheit
        w = wind_mph**0.16
        return 35.74 + 0.6215 * t - 35.75 * w + 0.4275 * t * w

    return fahrenheit
