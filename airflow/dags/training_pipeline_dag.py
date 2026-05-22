from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="customer_training_pipeline",
    description="Train and evaluate the customer churn baseline model.",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "training"],
) as dag:
    train_model = BashOperator(
        task_id="train_churn_model",
        bash_command=(
            "python /opt/airflow/project/scripts/run_training_pipeline.py "
            "--input /opt/airflow/project/data/processed/features.csv "
            "--artifact-dir /opt/airflow/project/artifacts"
        ),
    )

    train_model
