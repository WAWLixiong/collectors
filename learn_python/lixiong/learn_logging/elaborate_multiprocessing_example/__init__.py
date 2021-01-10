#!/usr/bin/env python3
# coding:utf-8

import logging
import logging.config
import logging.handlers
import os
import random
import time
from multiprocessing import Process, Queue, Event, current_process

class MyHandler:

    def handle(self, record):
        logger = logging.getLogger(record.name)
        record.processName = '{} (for {})'.format(current_process().name, record.processName)
        logger.handle(record)

def listener_process(q, stop_event, config):

    logging.config.dictConfig(config)
    listener = logging.handlers.QueueListener(q, MyHandler())
    listener.start()
    if os.name == 'posix':
        logger = logging.getLogger('setup')
        logger.critical('Should not appear, because of disabled logger')
    stop_event.wait()
    listener.stop()

def worker_process(config):
    logging.config.dictConfig(config)
    levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    loggers = [
        'foo', 'foo.bar', 'foo.bar.baz', 'spam', 'spam.ham', 'spam.ham.eggs',
    ]
    if os.name == 'posix':
        logger = logging.getLogger('setup')
        logger.critical('Should not appear, because of disabled logger ...')
    for i in range(100):
        lvl = random.choice(levels)
        logger = logging.getLogger(random.choice(loggers))
        logger.log(lvl, 'Message no. {}'.format(i))
        time.sleep(0.01)

def main():
    q = Queue()
    # The main process gets a simple configuration which prints to the console.
    config_inital = {
        'version': 1,
        'formatters': {
            'detailed': {
                'class':'logging.Formatter',
                'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
            }
        },
        'handlers':{
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
    # The worker process configuration is just a QueueHandler attached to the
    # root logger, which allows all messages to be sent to the queue.
    # We disable existing loggers to disable the "setup" logger used in the
    # parent process. This is needed on POSIX because the logger will
    # be there in the child following a fork().

    config_worker = {
        'version': 1,
        'disable_existing_loggers': True,
        'handlers': {
            'queue': {
                'class': 'logging.handlers.QueueHandler',
                'queue': q,
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['queue']
        },
    }
    # The listener process configuration shows that the full flexibility of
    # logging configuration is available to dispatch events to handlers however
    # you want.
    # We disable existing loggers to disable the "setup" logger used in the
    # parent process. This is needed on POSIX because the logger will
    # be there in the child following a fork().
    config_listener = {
        'version': 1,
        'formatters': {
            'detailed': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
            },
            'simple': {
                'class': 'logging.Formatter',
                'format': '%(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'simple',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': './log/mplog.log',
                'mode': 'w',
                'formatter': 'detailed',
            },
            'foofile': {
                'class': 'logging.FileHandler',
                'filename': './log/mplog-foo.log',
                'mode': 'w',
                'formatter': 'detailed',
            },
            'errors': {
                'class': 'logging.FileHandler',
                'filename': './log/mplog-errors.log',
                'mode': 'w',
                'level': 'ERROR',
                'formatter': 'detailed',
            },
        },
        'loggers': {
            'foo': {
                'handlers': ['foofile']
            },
            'root': {
                'level': 'DEBUG',
                'handlers': ['console', 'file', 'errors']
            }
        }
    }

    logging.config.dictConfig(config_inital)
    logger = logging.getLogger('setup')
    logger.info('About to create workers')
    workers = []
    for i in range(5):
        wp = Process(target=worker_process, name='worker: {}'.format(i + 1),
                     args=(config_worker,) )
        workers.append(wp)
        wp.start()
        logger.info('started worker: {}'.format(wp.name))
    logger.info('About to create listener ...')
    stop_event = Event()
    lp = Process(target=listener_process, name='listener',
                 args=(q, stop_event, config_listener))
    lp.start()
    logger.info('Started listener')
    for wp in workers:
        wp.join()
    # Workers all done, listening can now stop.
    # Logging in the parent still works normally.
    logger.info('Telling listener to stop ...')
    stop_event.set()
    lp.join()
    logger.info('All done')

if __name__ == '__main__':
    main()
