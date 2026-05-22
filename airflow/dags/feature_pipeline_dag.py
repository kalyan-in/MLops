from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="customer_feature_pipeline",
    description="Create model-ready customer feature data.",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "features"],
) as dag:
    build_features = BashOperator(
        task_id="build_customer_features",
        bash_command=(
            "python /opt/airflow/project/scripts/run_feature_pipeline.py "
            "--input /opt/airflow/project/data/sample/customers.csv "
            "--output /opt/airflow/project/data/processed/features.csv"
        ),
    )

    build_features
