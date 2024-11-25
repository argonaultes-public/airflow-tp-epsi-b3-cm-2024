from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(dag_id='empty'):
    EmptyOperator(task_id='empty_task')