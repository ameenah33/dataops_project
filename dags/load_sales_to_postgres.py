from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def load_csv_to_postgres():
    df = pd.read_csv('/opt/airflow/data/sales.csv') 
    engine = create_engine("postgresql://amina:amina@host.docker.internal:5432/sales_db")  
    df.to_sql('raw_sales', engine, if_exists='replace', index=False)
    print("✅ Données chargées dans PostgreSQL")

with DAG(
    dag_id='load_sales_to_postgres',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    description='Charge les ventes  CSV vers PostgreSQL tous les jours',
) as dag:

    task_ingest = PythonOperator(
        task_id='load_csv',
        python_callable=load_csv_to_postgres
    )

    task_ingest
