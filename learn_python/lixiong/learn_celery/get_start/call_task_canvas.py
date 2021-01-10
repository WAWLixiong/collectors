from learn_python.lixiong.learn_celery.get_start.tasks import add
from learn_python.lixiong.learn_celery.get_start.tasks import app
from celery import group

group(add.s(i, i ) for i in range(10))().get()
# >>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]



