from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain
from airflow.utils.trigger_rule import TriggerRule

@dag()
def testdeco():
    t1 = BashOperator(
        task_id='testdecotask1',
        bash_command='echo "hello" && exit 1')
    t2 = BashOperator(
        task_id='testdecotask2',
        bash_command='echo "after task1"'
    )
    t3 = BashOperator(
        task_id='testdecotask3',
        bash_command='echo "triggered only on error"',
        trigger_rule=TriggerRule.ALL_FAILED
    )
    chain(t1, [t2, t3])

testdeco()