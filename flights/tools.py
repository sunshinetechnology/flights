"""flights.tools

Adds support for working with FlightRecords.
"""
import csv
import typing as t
from io import TextIOWrapper
from pathlib import Path

from flights.data import FlightRecord


def data_iter(
    data: t.List[FlightRecord],
) -> t.Generator[None, None, t.Dict[str, t.Any]]:
    """Returns a generator where each yield is a FlightRecord as a dict."""
    for record in data:
        yield record.asdict


def write_data(text_writer: TextIOWrapper, data: t.List[FlightRecord]) -> Path:
    """Writes eac FlightRecord in `data` with `text_writer`."""
    with text_writer as csv_writer:
        fieldnames: t.List[str] = list(data[0].asdict.keys())
        writer: csv.DictWriter = csv.DictWriter(
            csv_writer, delimiter="|", fieldnames=fieldnames
        )
        writer.writerows(list(data_iter(data)))
