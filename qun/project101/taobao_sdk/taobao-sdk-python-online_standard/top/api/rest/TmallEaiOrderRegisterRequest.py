'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class TmallEaiOrderRegisterRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.action = None
		self.data_mode = None
		self.event_name = None
		self.topic = None
		self.user_type = None

	def getapiname(self):
		return 'tmall.eai.order.register'
