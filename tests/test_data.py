"""tests.test_data

Adds support for flights.data tests.
"""
import typing as t
from datetime import datetime

from flights import data


# Typing.
FlightRecord = t.NewType("FlightRecord", data.FlightRecord)


class TestFlightRecord:
    """Tests data.FlightRecord."""

    def test_init(self):
        """Test FlightRecord is initialized."""
        obj: FlightRecord = data.FlightRecord(
            "MAN", "JFK", datetime.now(), datetime.now(), "1233", 99.99, "STND", 9, "O"
        )
        assert hasattr(obj, "departing")
        assert hasattr(obj, "arriving")
        assert hasattr(obj, "departing_at")
        assert hasattr(obj, "arriving_at")
        assert hasattr(obj, "code")
        assert hasattr(obj, "fare")
        assert hasattr(obj, "fare_type")
        assert hasattr(obj, "seats")
        assert hasattr(obj, "direction")
