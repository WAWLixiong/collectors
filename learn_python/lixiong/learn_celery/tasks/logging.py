"""
A special logger is available named “celery.task”,
you can inherit from this logger to automatically get the task name and unique id as part of the logs.
"""

# todo:现在会报ModuleNotFoundError: No module named 'logging.handlers'; 'logging' is not a package
# from celery.utils.log import get_task_logger
from celery import Celery

# logger = get_task_logger(__name__)
app = Celery()

@app.task
def add(a, b):
    # logger.info('Add {} + {}'.format(a, b))
    return a + b


# if __name__ == '__main__':
#     ret = add(1, 2)
#     print(ret)
