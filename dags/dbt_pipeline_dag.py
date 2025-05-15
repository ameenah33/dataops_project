from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'amina',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dbt_sales_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    description='Pipeline DBT pour les ventes'
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /opt/airflow/dbt && dbt run'
    )

    dbt_test = BashOperator(
        task_id='test_dbt_models',
        bash_command='cd /opt/airflow/dbt && dbt test'
    )

    dbt_run >> dbt_test
