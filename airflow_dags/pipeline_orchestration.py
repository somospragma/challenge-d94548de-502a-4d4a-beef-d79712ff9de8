from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.load_data import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('pipeline_orchestration', default_args=default_args, schedule_interval='@daily') as dag:
    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )
    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )
    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    extract >> transform >> load