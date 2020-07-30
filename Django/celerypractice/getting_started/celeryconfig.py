#!usr/bin/python
# -*- coding:utf8 -*-
"""
you can tell your celery instance to user a configuration module by calling
the app.config_from_object() method
"""


broker_url = 'redis://127.0.0.1:6379/3'
result_backend = 'redis://127.0.0.1:6379/0'

task_serializer = 'json'
result_serializer = 'json'
