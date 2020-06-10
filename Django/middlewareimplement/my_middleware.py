# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2020-06-10 18:39:52
# @Last Modified by:   Clarence
# @Last Modified time: 2020-06-10 18:46:26
# 中间件的简单实现
class Router(obejct):
	def __init__(self):
		self.path_info = {}

	def route(self, environ, start_response):
		application = self.path_infp[environ['PATH_INFO']]
		return application(environ, start_response)

	def __call__(self, path):
		def wrapper(application):
			self.path_info[path] = application 
		return wrapper 

router = Router()