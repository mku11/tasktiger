import tasks
import tasktiger

tiger = tasktiger.TaskTiger()
for i in range(6):
    tiger.delay(tasks.hello_batch, args=(str(i),), queue="my_batch_queue")
