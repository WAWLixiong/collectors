"""
retry it’ll send a new message,
using the same task-id, and it’ll take care to make sure the message is delivered to the same queue
 as the originating task.
"""

from celery import Celery
app = Celery()

class Twitter:
    def __init__(self, oauth):
        pass

    def set_status(self, tweet):
        pass

@app.task(bind=True)
def send_twitter_status(self, oauth, tweet):
    try:
        twitter = Twitter(oauth)
        twitter.set_status(tweet)
    except Exception as exc:
        raise self.retry(exc=exc)

# -----------------------------------------
def something_raising():
    pass

# unit is second
@app.task(bind=True, default_retry_delay=30 * 60)  # retry in 30 minutes.
def add(self, x, y):
    try:
        something_raising()
    except Exception as exc:
        # overrides the default delay to retry after 1 minute
        raise self.retry(exc=exc, countdown=60, max_retries=3)

# -----------------------------------------
# auto retry for known exceptions

@app.task(autoretry_for=(ValueError,), retry_kwargs={'max_retriex':5}) # Exception
def add(x, y):
    return x + y

