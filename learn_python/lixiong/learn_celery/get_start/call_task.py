from learn_python.lixiong.learn_celery.get_start.tasks import add
# from learn_python.lixiong.learn_celery.get_start.tasks import app
# import pprint

# print(add.name)
# pprint.pprint(app.tasks)
# 其中有一项如下：
#  'learn_python.lixiong.learn_celery.get_start.tasks.add': <@task: learn_python.lixiong.learn_celery.get_start.tasks.add of tasks at 0x7f387bdae4a8>}

# delay 是apply_async方法的快捷方式
result = add.delay(4, 4)
# result = add.apply_async((4, 4), queue='help me', countdown=10)
print(result)
print(result.backend) # 查看后端信息
print(result.id) # 查看任务id

# 调用以下函数以后发现结果队列就会被删除, 应该是因为队列属性设置了auto-delete，队列内没有消息后就会自动删除队列
# print(result.get(timeout=12)) # 可想而知，这里就是从结果队列中获取消息
# print(result.get()) # 可想而知，这里就是从结果队列中获取消息
# print(result.get(propagate=False)) # propagate=False 会返回 exception 实例，如果想要确认任务成功失败，需要调用查询接口
# result.failed()
# result.successful()
# result.state >>> 'FAILURE'
# print(result.traceback)

# A task can only be in a single state, but it can progress through several states. The stages of a typical task can be:
# PENDING -> STARTED -> SUCCESS

# ret = app.AsyncResult('this-id-does-not-exist')
# 任务的默认状态就是 PENDING，未知任务的状态都是 PENDING
# ret.state >>> 'PENDING'

# a retry task's state may be the following
# PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS

# signature

# add.signature((2, 2), countdown=10) # >>> tasks.add(2, 2)
# the shortcut
# add.s(2, 2) >>> tasks.add(2, 2)

