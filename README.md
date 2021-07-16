# flights

Flights is a package to simplify working with flight data at Sunshine Technology.

## installation
```
gh repo clone sunshinetechnology/flights
cd flights
pipenv install .
```
or
```
pipenv install git+https://github.com/sunshinetechnology/flights.git#egg=flights
```

## usage
Flights contains two modules;
 - data - adds support for the FlightRecord dataclass
 - tools - adds support for working with FlightRecords

For usage see `help(flights.data)` and `help(flights.tools)` in your Python console.