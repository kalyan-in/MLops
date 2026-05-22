from __future__ import annotations

import json
import math
from pathlib import Path

from kalyan_mlops.features import FEATURE_COLUMNS


Model = dict[str, dict[str, float]]


def train_centroid_classifier(rows: list[dict[str, float]]) -> Model:
    grouped: dict[str, list[dict[str, float]]] = {"0": [], "1": []}
    for row in rows:
        label = str(int(row["churned"]))
        if label not in grouped:
            raise ValueError(f"unsupported label: {label}")
        grouped[label].append(row)

    if not grouped["0"] or not grouped["1"]:
        raise ValueError("training data must include both churn classes")

    return {label: _centroid(label_rows) for label, label_rows in grouped.items()}


def predict(model: Model, row: dict[str, float]) -> int:
    distances = {
        label: _distance(row, centroid)
        for label, centroid in model.items()
    }
    return int(min(distances, key=distances.get))


def evaluate(model: Model, rows: list[dict[str, float]]) -> dict[str, float]:
    if not rows:
        raise ValueError("evaluation data cannot be empty")

    correct = 0
    for row in rows:
        correct += int(predict(model, row) == int(row["churned"]))

    return {
        "accuracy": round(correct / len(rows), 4),
        "examples": float(len(rows)),
    }


def save_artifacts(model: Model, metrics: dict[str, float], artifact_dir: str | Path) -> None:
    output_dir = Path(artifact_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "model.json").write_text(json.dumps(model, indent=2), encoding="utf-8")
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")


def _centroid(rows: list[dict[str, float]]) -> dict[str, float]:
    return {
        column: round(sum(row[column] for row in rows) / len(rows), 6)
        for column in FEATURE_COLUMNS
    }


def _distance(row: dict[str, float], centroid: dict[str, float]) -> float:
    squared = [(row[column] - centroid[column]) ** 2 for column in FEATURE_COLUMNS]
    return math.sqrt(sum(squared))
