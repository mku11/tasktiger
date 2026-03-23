from tasktiger import TaskTiger

# concurrent
tiger = TaskTiger(setup_structlog=True)
tiger.run_worker()
