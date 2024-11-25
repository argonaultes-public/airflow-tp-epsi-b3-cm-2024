from airflow import DAG
from airflow.operators.empty import EmptyOperator

from datetime import datetime as dt
from datetime import timedelta

with DAG(
    dag_id='empty_schedule_timedelta',
    schedule=timedelta(seconds=20),
    start_date=dt(2024,11,1),
    is_paused_upon_creation=True,
    catchup=False
    ):
    t1 = EmptyOperator(task_id='empty_task')
    t2 = EmptyOperator(task_id='empty_task_2')
    t1 >> t2

# * * * * * <command to execute>
# | | | | |
# | | | | day of the week (0–6) (Sunday to Saturday; 
# | | | month (1–12)             7 is also Sunday on some systems)
# | | day of the month (1–31)
# | hour (0–23)
# minute (0–59)


with DAG(
    dag_id='empty_schedule_cron',
    schedule='* * * * *', #
    start_date=dt(2024,11,1),
    is_paused_upon_creation=True,
    catchup=False
    ):
    t1 = EmptyOperator(task_id='empty_task')
    t2 = EmptyOperator(task_id='empty_task_2')
    t1 >> t2

with DAG(
    dag_id='empty_catchup_enabled',
    schedule='* * * * *',
    start_date=dt(2024,11,25),
    is_paused_upon_creation=True,
    catchup=True
    ):
    t1 = EmptyOperator(task_id='empty_task')
    t2 = EmptyOperator(task_id='empty_task_2')
    t1 >> t2