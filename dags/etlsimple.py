from airflow import DAG
from airflow.datasets import Dataset

from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.python import PythonOperator

from datetime import datetime
import json

def read_file_in_json():
    with open('/tmp/resp.json', 'r') as f:
        return str(json.load(f)).replace('\'', '"')

with DAG(
    dag_id='load_data_into_db',
    schedule=[Dataset('file://res.json')],
    is_paused_upon_creation=False,
    start_date=datetime(2020,1,1),
    catchup=False):

    PythonOperator(
        task_id='read_file',
        python_callable=read_file_in_json
    )

    SQLExecuteQueryOperator(
        task_id='insert_data',
        conn_id='db_postgres_crm',
        sql="INSERT INTO customers_json VALUES ('{{task_instance.xcom_pull(task_ids='read_file')}}'::json)"
    )
