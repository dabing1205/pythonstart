#!/usr/bin/python
#encoding=GBK
import HTMLParser
import sys

s= '中国'
print s, type(s), repr(s) #.decode('utf-8')

s = u'中国'
print s, type(s), repr(s)

f= r'D:\PythonStart\windows\Development_Report_1.html'
t = open(f).read().decode('utf8')
print  type(t), repr(t), 
print t
f = open('test.txt', 'w')
f.write(t.encode('GBK'))
f.close()

'''
f= r'D:\PythonStart\windows\Development_Report_1.html'
t = open(f).read().decode('utf8')
print repr(t)
print t
'''
'''
print sys.getdefaultencoding()
#你好

f = open(r'D:\PythonStart\windows\Development_Report_1.html')
s = f.read()
f.close()
print type(s) # <type 'str'>
u = s.decode('UTF-8')
f = open('test.txt', 'w')
s = u.encode('GBK')
f.write(s)
f.close()
'''
'''
parser.feed()
parser.close()
print parser.anchorlist
'''