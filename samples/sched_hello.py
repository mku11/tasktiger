from tasktiger import TaskTiger
import tasks

for i in range(6):
    tiger = TaskTiger()
    # tiger.delay(tasks.hello, args=(str(i),), unique=True)
    tiger.delay(tasks.hello, args=(str(i),))
