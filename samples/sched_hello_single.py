from tasktiger import TaskTiger
import tasks

tiger = TaskTiger()
# tiger.delay(tasks.hello, args=(str(i),), unique=True)
tiger.delay(tasks.hello, args=("test",))
