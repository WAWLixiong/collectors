from __future__ import absolute_import, unicode_literals
from celery import Celery


# The include argument is a list of modules to import when the worker starts.
# You need to add our tasks module here so that the worker is able to find our tasks.
include = ['learn_python.lixiong.learn_celery.project.tasks']

# 在collectors目录下执行命令如下，就可以自动找到所有的task
# celery -A learn_python.lixiong.learn_celery.project worker -l debug
app = Celery('proj', include=include)
app.config_from_object('learn_python.lixiong.learn_celery.base_config')
app.conf.update(result_expires=3600)


if __name__ == '__main__':
    app.start()
