mq_user = 'zzlion'
mq_password = 'lixiong6660'
# mq_host = '47.96.156.169'
mq_host = 'localhost'
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

task_routes = {
    'learn_python.lixiong.learn_celery.get_start.tasks.add': 'low-priority',
    # 'learn_python.lixiong.learn_celery.get_start.tasks.add': {'rate_limit': '10/m'},
}
