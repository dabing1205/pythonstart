'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class TravelItempropsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.pid = None

	def getapiname(self):
		return 'taobao.travel.itemprops.get'
