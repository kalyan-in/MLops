# Architecture

The project is split into three layers.

## Pipeline Entry Points

The `scripts/` directory contains command-line entry points. These scripts are what local users, CI jobs, Docker commands, and Airflow tasks run.

## Application Package

The `src/kalyan_mlops/` package contains reusable code for data loading, feature engineering, and training. Keeping logic in importable modules makes the project easier to test and avoids putting business logic directly inside DAG files.

## Orchestration

The Airflow DAGs are thin wrappers around the command-line scripts. This keeps scheduling concerns separate from pipeline logic and makes the same code runnable both locally and in Airflow.

## Artifact Flow

Raw customer records are read from `data/sample/customers.csv`. The feature job writes `data/processed/features.csv`. The training job writes `artifacts/model.json` and `artifacts/metrics.json`.
