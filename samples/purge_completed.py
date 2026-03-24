from tasktiger import TaskTiger
from tasktiger._internal import COMPLETED
from tasktiger.task import Task

tiger = TaskTiger()
_, tasks = Task.tasks_from_queue(
    tiger,
    "default",
    COMPLETED,
    include_not_found=True,
)

for task in tasks:
    try:
        task.delete()
        print("deleted:", task.id)
    except:
        print("cannot delete:", task.id)