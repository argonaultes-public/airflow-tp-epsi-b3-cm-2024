from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(dag_id='empty'):
    t1 = EmptyOperator(task_id='empty_task')
    t2 = EmptyOperator(task_id='empty_task_2')
    t1 >> t2