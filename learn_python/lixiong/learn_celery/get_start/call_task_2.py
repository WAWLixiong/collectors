from learn_python.lixiong.learn_celery.get_start.tasks import add


result = add.delay(4, 4)
# result = add.apply_async((4, 4), queue='help me', countdown=10)
print(result)
print(result.backend) # 查看后端信息
print(result.id) # 查看任务id

# print(result.get(timeout=2))
print(result.failed())
