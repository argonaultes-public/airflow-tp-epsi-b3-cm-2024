from airflow import DAG
from airflow.sensors.filesystem import FileSensor

from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
import json
import os


def read_file_in_json():
    file_path = '/opt/airflow/data/filetolisten.json'
    with open(file_path, 'r') as f:
        result = str(json.load(f)).replace('\'', '"')
    os.remove(file_path)
    return result

with DAG(
    dag_id='file_sensor_test',
    schedule=timedelta(seconds=5),
    start_date=datetime(2020, 1, 1),
    is_paused_upon_creation=False,
    catchup=False
    ):
    task_sensor = FileSensor(
        task_id='listen_resp',
        poke_interval=timedelta(milliseconds=500),
        timeout=5,
        filepath='/opt/airflow/data/filetolisten.json'
    )
    task_read_file = PythonOperator(
        task_id='listen_read_file',
        python_callable=read_file_in_json
    )

    task_insert_data = SQLExecuteQueryOperator(
        task_id='listen_insert_data',
        conn_id='db_postgres_crm',
        sql="INSERT INTO customers_json VALUES ('{{task_instance.xcom_pull(task_ids='listen_read_file')}}'::json)"
    )
    task_sensor >> task_read_file >> task_insert_data