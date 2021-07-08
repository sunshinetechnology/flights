from io import TextIOWrapper
from pathlib import Path
import typing as t
from datetime import datetime
from pytest import fixture

from flights import data, tools

# Typing.
FlightRecord = t.NewType("FlightRecord", data.FlightRecord)
RecordList = t.NewType("RecordList", t.List[FlightRecord])


@fixture
def record_list() -> RecordList:
    timestamp: datetime = datetime(2021, 3, 18, 1, 0, 0, 0)
    return [
        data.FlightRecord(
            "MAN", "JFK", timestamp, timestamp, "1233", 99.99, 9, "O"
        ),
        data.FlightRecord(
            "JFK", "MAN", timestamp, timestamp, "1233", 99.99, 9, "I"
        ),
    ]


def test_data_iter(record_list: RecordList):
    """Test data_iter yields."""
    expecting: t.List[t.Dict[str, t.Any]] = [
        {
            "departing": "MAN",
            "arriving": "JFK",
            "departing_date": "2021-03-18",
            "departing_time": "01:00:00",
            "arriving_date": "2021-03-18",
            "arriving_time": "01:00:00",
            "code": "1233",
            "fare": 99.99,
            "seats": 9,
            "direction": "O",
        },
        {
            "departing": "JFK",
            "arriving": "MAN",
            "departing_date": "2021-03-18",
            "departing_time": "01:00:00",
            "arriving_date": "2021-03-18",
            "arriving_time": "01:00:00",
            "code": "1233",
            "fare": 99.99,
            "seats": 9,
            "direction": "I",
        },
    ]
    actual: t.List[t.Dict[str, t.Any]] = list(tools.data_iter(record_list))
    assert actual == expecting


def test_write_data(tmp_path: Path, record_list: RecordList):
    """Test write_data outputs."""
    file_path: Path = tmp_path.joinpath("test.txt")

    writer: TextIOWrapper = file_path.open("w", newline="")
    tools.write_data(writer, record_list)
    writer.close()

    expecting: t.List[str] = [
        "MAN|JFK|1233|2021-03-18|01:00:00|2021-03-18|01:00:00|99.99|9|O\n",
        "JFK|MAN|1233|2021-03-18|01:00:00|2021-03-18|01:00:00|99.99|9|I\n",
    ]

    with file_path.open() as reader:
        actual: t.List[str] = reader.readlines()

    assert actual == expecting
