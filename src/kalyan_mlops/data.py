from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


Record = dict[str, str]


def read_csv_records(path: str | Path) -> list[Record]:
    csv_path = Path(path)
    with csv_path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv_records(path: str | Path, rows: Iterable[dict[str, object]]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    materialized_rows = list(rows)

    if not materialized_rows:
        output_path.write_text("", encoding="utf-8")
        return

    fieldnames = list(materialized_rows[0].keys())
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(materialized_rows)


def split_rows(rows: list[dict[str, float]], test_ratio: float = 0.25) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    if not 0 < test_ratio < 1:
        raise ValueError("test_ratio must be between 0 and 1")
    if len(rows) < 2:
        raise ValueError("at least two rows are required")

    test_size = max(1, round(len(rows) * test_ratio))
    split_at = len(rows) - test_size
    return rows[:split_at], rows[split_at:]
