'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class SimbaCampaignUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.nick = None
		self.online_status = None
		self.title = None

	def getapiname(self):
		return 'taobao.simba.campaign.update'
