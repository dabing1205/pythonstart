'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class AlipayMicropayOrderUnfreezeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.alipay_order_no = None
		self.auth_token = None
		self.memo = None

	def getapiname(self):
		return 'alipay.micropay.order.unfreeze'
