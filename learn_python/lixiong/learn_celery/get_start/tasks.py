from celery import Celery
from celery import Task
from celery.utils.log import get_task_logger
import time

# 第一个参数一般为当前模块的名字
app = Celery('hhhh')
app.config_from_object('learn_python.lixiong.learn_celery.get_start.celeryconfig')

logger = get_task_logger(__name__)

class DebugTask(Task):
    def __call__(self, *args, **kwargs):
        print('TASK STARTING: {}[{}]'.format(self.name, self.request.id))
        return self.run(*args, **kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

class MyCelery(Celery):

    def gen_task_name(self, name, module):
        if module.endswith('.tasks'):
            module = module[:-6]
        return super().gen_task_name(name, module)

# @app.task(ignore_result=True) # 不需要返回结果
# @app.task
@app.task(bind=True, base=DebugTask, queue='help me')
def add(self, a, b):
    print(self.request.id)
    logger.info(self.request.id)
    return 'hello world: a + b = {}'.format(a + b)

@app.task(bind=True, base=DebugTask)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state='PROGRESS', meta={'progress': 50})
    time.sleep(1)
    self.update_state(state='PROGRESS', meta={'progress': 90})
    time.sleep(1)
    return 'hello world : {}'.format(a + b)
# print(add.__class__.__mro__)

# print(add.name) # >>> hhhh.add, 在其他模块中是 >>> learn_python.lixiong.learn_celery.get_start.tasks.add

# 配置app硬编码的形式
# app.conf.task_serializer = 'json'
# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )
