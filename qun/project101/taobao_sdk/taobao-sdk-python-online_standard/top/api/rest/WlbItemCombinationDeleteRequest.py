'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class WlbItemCombinationDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.dest_item_list = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.wlb.item.combination.delete'
