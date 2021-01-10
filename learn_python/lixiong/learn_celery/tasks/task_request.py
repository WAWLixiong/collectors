"""
id:	The unique id of the executing task.
group: The unique id of the task’s group, if this task is a member.
chord: The unique id of the chord this task belongs to (if the task is part of the header).
correlation_id:	Custom ID used for things like de-duplication.
args: Positional arguments.
kwargs: Keyword arguments.
origin:	Name of host that sent this task.
retries: How many times the current task has been retried. An integer starting at 0.
is_eager: Set to True if the task is executed locally in the client, not by a worker.
eta: 预计最晚到达时间The original ETA of the task (if any). This is in UTC time (depending on the enable_utc setting).
expires: The original expiry time of the task (if any). This is in UTC time (depending on the enable_utc setting).
hostname: Node name of the worker instance executing the task.
delivery_info: Additional message delivery information. This is a mapping containing the exchange and routing key used to deliver this task. Used by for example app.Task.retry() to resend the task to the same destination queue. Availability of keys in this dict depends on the message broker used.
reply-to: Name of queue to send replies back to (used with RPC result backend for example).
called_directly: This flag is set to true if the task wasn’t executed by the worker.
timelimit: A tuple of the current (soft, hard) time limits active for this task (if any).
callbacks: A list of signatures to be called if this task returns successfully.
errback: A list of signatures to be called if this task fails.
utc: Set to true the caller has UTC enabled (enable_utc).

New in version 3.1.
headers: Mapping of message headers sent with this task message (may be None).
reply_to: Where to send reply to (queue name).
correlation_id: Usually the same as the task id, often used in amqp to keep track of what a reply is for.

New in version 4.0.
root_id: The unique id of the first task in the workflow this task is part of (if any).
parent_id: The unique id of the task that called this task (if any).
chain: Reversed list of tasks that form a chain (if any). The last item in this list will be the next task to succeed the current task. If using version one of the task protocol the chain tasks will be in request.callbacks instead.
"""

from celery import Celery

app = Celery()

@app.task(bind=True)
def add(self, a, b):
    print('excuting task id:{}\n args:{!r}\nkwargs:{!r}\n'.format(
        self.request.id, self.request.args, self.request.kwargs,
    ))
    return a + b
