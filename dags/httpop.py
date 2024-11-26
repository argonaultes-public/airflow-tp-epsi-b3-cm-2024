from airflow import DAG

from datetime import datetime

from airflow.providers.http.operators.http import HttpOperator


with DAG(
    dag_id='dag_access_log',
    start_date=datetime.now(),
    schedule=None,
    is_paused_upon_creation=False):
    read_http_file = HttpOperator(
        task_id='get_access_log',
        http_conn_id='http_access_log',
        method='GET',
        endpoint='assets/access.log.1',
        response_filter=lambda response : '\n'.join([line for line in response.text.split('\n') if 'GET /recover.html' in line])
    )