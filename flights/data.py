"""flights.data

Adds support for the FlightRecord dataclass.
"""
import typing as t
from dataclasses import dataclass
from datetime import datetime


@dataclass
class FlightRecord:
    """Class representation of a flight record."""

    departing: str
    arriving: str
    departing_at: datetime
    arriving_at: datetime
    code: str
    fare: float
    fare_type: str
    seats: int
    direction: str

    @property
    def asdict(self) -> t.Dict[str, t.Any]:
        return {
            "departing": self.departing,
            "arriving": self.arriving,
            "code": self.code,
            "departing_date": self.departing_at.strftime("%Y-%m-%d"),
            "departing_time": self.departing_at.strftime("%H:%M:%S"),
            "arriving_date": self.arriving_at.strftime("%Y-%m-%d"),
            "arriving_time": self.arriving_at.strftime("%H:%M:%S"),
            "fare": self.fare,
            "seats": self.seats,
            "direction": self.direction,
        }
