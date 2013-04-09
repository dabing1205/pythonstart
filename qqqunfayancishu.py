#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Encore Hu, <huyoo353@126.com>'
'''
使用方法:
1. 在消息管理中, 选中你的群, 右键菜单选择 导出聊天记录
2. 在弹出的保存文件框中选择保存格式为 文本格式txt, 文件名为fffff.txt
3. 将本脚本放在你导出的文件相同的目录, 在idle中执行即可.
'''
import re
patten_timestamp = ur'\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2} ([\w\u4e00-\u9fa5\(\)\.]*\(\d+\))'

ff=open('fffff.txt','r')
text=ff.read()
ff.close()
text=text.decode('utf-8')
p_timestamp=re.compile(patten_timestamp)
#print repr(text[:200])

fanyancishu = {}
find_list = p_timestamp.findall(text)

for x in  find_list:
    x=x.strip()
    fanyancishu[x] = fanyancishu.get(x, 0) + 1


lll=[(k,v) for k,v in fanyancishu.items()]
lll.sort(cmp=lambda x,y :cmp(-x[1],-y[1]))
for xxx in lll:
    print xxx[0],xxx[1]
