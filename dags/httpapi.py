from airflow import DAG
from airflow.datasets import Dataset

from datetime import datetime

from airflow.providers.http.operators.http import HttpOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import json

def process_json_data(task_instance):
    with open('/tmp/resp.json', 'w') as f:
        f.write(json.dumps(task_instance.xcom_pull(task_ids='get_api_data')))

with DAG(
    dag_id='dag_api_data',
    start_date=datetime.now(),
    schedule=None,
    is_paused_upon_creation=False):
    read_http_file = HttpOperator(
        task_id='get_api_data',
        http_conn_id='http_api_test',
        method='GET',
        endpoint='/profiles',
        response_filter=lambda response : response.json()[1],
        log_response=True
    )
    write_to_file_bash = BashOperator(
        task_id='write_to_file_bash',
        bash_command="sleep 10 && echo {{ task_instance.xcom_pull(task_ids='get_api_data') }} > /tmp/res.json"
        )
    write_to_file_python = PythonOperator(
        task_id='write_to_file_python',
        python_callable=process_json_data,
        outlets=[Dataset('file://res.json')])
    read_http_file >> [write_to_file_bash, write_to_file_python]