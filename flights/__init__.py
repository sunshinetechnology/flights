"""
Flights is a package to simplify working with flight data at Sunshine Technology.

It is made up for two modules;

    data - adds support for the FlightRecord dataclass

    tools - adds support for working with FlightRecords

For usage see `help(flights.data)` and `help(flights.tools)`
"""

from flights import data, tools  # noqa: F401


__version__: str = "0.3.0"
