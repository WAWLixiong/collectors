"""
Any keyword argument passed to the task decorator will actually be set as an attribute of the resulting task class,
"""

# general
"""
TASK.anme
request
max_retreis
throws 预期的错误类型，logger等级为info，不会记录traceback
default_retry_delay 默认3 * 60
rate_limit
time_limit
soft_time_limit
ignore_result # Don’t store task state. Note that this means you can’t use AsyncResult to check if the task is ready, or get its return value.
store_errors_even_if_ignored # can be pickle json yaml
compression # can be gzip bzip2
backend
acks_late # Note: This means the task may be executed multiple times should the worker crash in the middle of execution. 
track_started
"""