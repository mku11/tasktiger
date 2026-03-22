from tasktiger import TaskTiger, periodic
import datetime

tiger = TaskTiger()

@tiger.task(schedule=periodic(minutes=1))
def purge_errored_tasks():
    tiger.purge_errored_tasks(
        limit=1000,
        last_execution_before=(
            datetime.datetime.utcnow() - datetime.timedelta(weeks=12)
        )
    )
