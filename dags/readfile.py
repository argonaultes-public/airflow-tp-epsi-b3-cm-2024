from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import timedelta
from datetime import datetime


def open_file():
    with open('/opt/airflow/data/access.log.1', 'r') as f:
        lines = f.readlines()
        print('\n'.join(lines))

with DAG(
    dag_id='readfile',
    schedule=timedelta(seconds=30),
    start_date=datetime.now(),
    is_paused_upon_creation=False
):
    t_file_bash = BashOperator(
        task_id='t_file_bash',
        bash_command='cat /opt/airflow/data/access.log.1'
    )
    t_file_python = PythonOperator(
        task_id='t_file_python',
        python_callable=open_file
    )