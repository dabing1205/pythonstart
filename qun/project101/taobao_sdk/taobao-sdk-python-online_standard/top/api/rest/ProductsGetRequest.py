'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class ProductsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.nick = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.products.get'
