'''
Created by auto_sdk on 2013-08-25 12:39:21
'''
from top.api.base import RestApi
class SimbaRptAdgroupkeywordeffectGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.campaign_id = None
		self.end_time = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.search_type = None
		self.source = None
		self.start_time = None
		self.subway_token = None

	def getapiname(self):
		return 'taobao.simba.rpt.adgroupkeywordeffect.get'
