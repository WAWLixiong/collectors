from celery import Celery

app = Celery()

@app.task
def add(a, b):
    return a + b

if __name__ == '__main__':
    app.delay(8, 8)
