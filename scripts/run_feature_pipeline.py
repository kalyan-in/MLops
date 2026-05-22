from __future__ import annotations

import argparse

from kalyan_mlops.data import read_csv_records, write_csv_records
from kalyan_mlops.features import build_feature_table


def main() -> None:
    parser = argparse.ArgumentParser(description="Build model-ready feature rows.")
    parser.add_argument("--input", required=True, help="Raw customer CSV path.")
    parser.add_argument("--output", required=True, help="Feature CSV output path.")
    args = parser.parse_args()

    rows = read_csv_records(args.input)
    features = build_feature_table(rows)
    write_csv_records(args.output, features)
    print(f"wrote {len(features)} feature rows to {args.output}")


if __name__ == "__main__":
    main()
