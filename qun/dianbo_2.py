#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib2
import re
import os
import urllib
import Queue
import json
import time
import sys
import threading
import random

id_list=[]
data_list=[]

ok_cookie=''

index1=0

site_url='http://www.1782.cc'
caiji_url=site_url+'/admini5/admin_20131001.asp?ac=list&rid=5'


#登录网站
def login(username,password):
    global ok_cookie

    headers={
        'Accept':'text/html, application/xhtml+xml, */*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'',
        'DNT':'1',
        'Host':'www.1782.cc',
        'Pragma':'no-cache',
        'Proxy-Connection':'Keep-Alive',
        'Referer':'http://www.1782.cc/admini5/index.asp?action=login',
        'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        }

    h=httplib2.Http(timeout=30)
    urlstr='http://www.1782.cc/admini5/index.asp?action=check'
    data="input_name="+username+"&input_pwd="+password+"&input_rem=true&input_sub=%B5%C7%C2%BC"
    response,content=h.request(urlstr,'POST',body=data,headers=headers)
    print(response)
    content=content.decode('gbk').encode('utf-8')
    #print(content)

    if content.find('index.asp')>0:
        print('login ok!')
    set_cookie=response['set-cookie']

    checkadmin1782='checkadmin'+re.findall(r'checkadmin(.*?);',set_cookie)[0]

    cookie1=checkadmin1782+'; m%5Fusername=admin1782'

    cookie2=re.findall(r'ASPSESSION(.*?);',set_cookie)[0]
    cookie2='; ASPSESSION'+cookie2
    ok_cookie=cookie1+cookie2


# 选定ID来采集数据。
def caiji(ids):
    headers={
        'Accept':'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, */*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN',
        'Cache-Control':'no-cache',
        'Connection':'Keep-Alive',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':ok_cookie,
        'Host':'www.1782.cc',
        'Referer':'http://www.1782.cc/admini5/admin_20131001.asp?ac=list&rid=5',
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
        }
    h=httplib2.Http(timeout=30)
    data={
        'ac':'select',
        'ids':ids,
        'rid':'5'
    }
    urlstr='http://www.1782.cc/admini5/admin_20131001.asp?'

    print(ok_cookie)
    response,content=h.request(urlstr,'POST',body=urllib.urlencode(data),headers=headers)
    #print(response)
    content=content.decode('gbk').encode('utf-8')
    print(content)
    if content.find('恭喜，全部搞定')>0:
        print('caiji ok!')

#生成地址
def make_html(ids):
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'Cookie':ok_cookie,
        'Host':'www.1782.cc',
        'Referer':'http://www.1782.cc/admini5/admin_20131001.asp?ac=list&rid=5&t=0&h=&wd=&pg=2',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:23.0) Gecko/20100101 Firefox/23.0',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    h=httplib2.Http(timeout=30)

    data={
        'm_id':ids,
        'movetype':'',
        'ptopic':'0',
        }
    urlstr=site_url+'/admini5/admin_makehtml.asp?action=selected'
    response,content=h.request(urlstr,'POST',body=urllib.urlencode(data),headers=headers)
    content=content.decode('gbk').encode('utf-8')
    print(response)
    print(content)


username='admin1782'
password='520123'
login(username,password)


#caiji(51394)



#问题描述：登录(login)网站后,获取cookie， 操作 caiji()  make_html 能提示成功，问题就这些了。
#网站后台：http://www.1782.cc/admini5/index.asp
#账号 admin1782
#密码 520123

















