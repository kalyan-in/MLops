from __future__ import annotations

import argparse

from kalyan_mlops.data import read_csv_records, split_rows
from kalyan_mlops.features import build_feature_table
from kalyan_mlops.train import evaluate, save_artifacts, train_centroid_classifier


def main() -> None:
    parser = argparse.ArgumentParser(description="Train and evaluate the baseline churn model.")
    parser.add_argument("--input", required=True, help="Feature CSV or raw customer CSV path.")
    parser.add_argument("--artifact-dir", default="artifacts", help="Directory for model and metrics.")
    args = parser.parse_args()

    raw_rows = read_csv_records(args.input)
    feature_rows = build_feature_table(raw_rows) if "total_spend" in raw_rows[0] else [
        {key: float(value) for key, value in row.items()}
        for row in raw_rows
    ]
    train_rows, test_rows = split_rows(feature_rows)
    model = train_centroid_classifier(train_rows)
    metrics = evaluate(model, test_rows)
    save_artifacts(model, metrics, args.artifact_dir)
    print(f"saved model artifacts to {args.artifact_dir}; accuracy={metrics['accuracy']}")


if __name__ == "__main__":
    main()
