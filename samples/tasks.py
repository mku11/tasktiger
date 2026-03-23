from tasktiger import TaskTiger
import time

tiger = TaskTiger()


def hello(text, duration=5):
    for i in range(duration):
        print("Hello", text, i)
        time.sleep(1)
    print("Hello end", text)
    # raise Exception("test error")


# @tiger.task(batch="my_batch_queue")
def hello_batch(name):
    print("Hello batch start", name)
    time.sleep(5)
    print("Hello batch end", name)
