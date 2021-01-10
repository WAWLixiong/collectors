from lixiong.learn_celery.get_start.tasks import hello

def on_raw_message(body):
    print(body)

a , b = 1, 1
r = hello.apply_async(args=(a, b))
print(r.get(on_message=on_raw_message, propagate=False))