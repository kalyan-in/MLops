# MLops

Original MLOps starter project for building, testing, scheduling, and packaging a small machine learning workflow.

## What This Project Does

This repository contains a complete lightweight MLOps workflow:

- validates and transforms raw CSV records
- creates model-ready feature rows
- trains a simple baseline classifier
- writes model artifacts and metrics
- schedules feature and training jobs with Airflow
- runs automated checks with GitHub Actions
- packages the project with Docker

The implementation is intentionally small so every part of the workflow is easy to inspect and extend.

## Project Layout

```text
.github/workflows/        CI workflow
airflow/dags/             Airflow DAG definitions
data/sample/              Small sample dataset for local runs
docs/                     Architecture notes
scripts/                  Pipeline entry points
src/kalyan_mlops/         Application package
tests/                    Unit tests
Dockerfile                Container image
docker-compose.yml        Local Airflow-oriented stack
requirements.txt          Python dependencies
```

## Quick Start

Create a virtual environment and install the project:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the feature pipeline:

```powershell
python scripts/run_feature_pipeline.py --input data/sample/customers.csv --output data/processed/features.csv
```

Train the baseline model:

```powershell
python scripts/run_training_pipeline.py --input data/processed/features.csv --artifact-dir artifacts
```

Run tests:

```powershell
pytest
```

## Pipeline Summary

The feature pipeline reads customer records and produces normalized numeric features. The training pipeline fits a compact centroid-based classifier, evaluates it on a holdout split, and saves both the model and metrics as JSON files.

## Next Improvements

- Add a real feature store or warehouse target.
- Replace the baseline model with scikit-learn or XGBoost.
- Add MLflow tracking for experiments.
- Add cloud storage inputs and outputs.
- Add deployment automation for batch inference.
