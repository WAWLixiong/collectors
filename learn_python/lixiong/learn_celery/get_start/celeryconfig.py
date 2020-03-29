
mq_user = 'zzlion'
mq_password = 'lixiong6660'
# mq_host = '47.96.156.169'
mq_host = 'www.zzlion.online' # caution 这里阿里云的服务器遇到个大坑，换成内外网都不行，但是单独测试mq连通性没问题
mq_port = 5672
mq_virtual_host = '/'

broker = 'amqp://{}:{}@{}:{}/{}'.format(mq_user, mq_password, mq_host, mq_port, mq_virtual_host)
broker_url = broker
result_backend = broker
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

# task_routes = {
    # 'learn_python.lixiong.learn_celery.get_start.tasks.add': 'low-priority', # 这项配置我有点没有搞懂
    # 'learn_python.lixiong.learn_celery.get_start.tasks.add': {'rate_limit': '10/m'},
    # 'learn_python.lixiong.learn_celery.get_start.tasks.add': {'queue': 'hipri'},
# }

# task_routes = ([
#     ('learn_python.lixiong.learn_celery.get_start.tasks.add', {
#         'queue': ''
#     }),
#     (),
#     (),
# ])