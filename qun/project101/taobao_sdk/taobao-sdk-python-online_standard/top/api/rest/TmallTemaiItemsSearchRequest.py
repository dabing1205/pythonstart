'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class TmallTemaiItemsSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cat = None
		self.sort = None
		self.start = None

	def getapiname(self):
		return 'tmall.temai.items.search'
