from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='test1',
    schedule=None,
    is_paused_upon_creation=True) as dag:
    BashOperator(
        task_id='hello',
        bash_command='echo "hello world"')