from tasktiger import TaskTiger

# batch
tiger = TaskTiger(
    setup_structlog=True,
    config={
        "BATCH_QUEUES": {
            "my_batch_queue": 2,
        },
    },
)
tiger.run_worker()
