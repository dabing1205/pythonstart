#!/usr/bin/env python
# -*- coding: utf-8

from sgmllib import SGMLParser
import formatter

class Parser(SGMLparser):
	def init_parser (self, filename):
		self.file = filename
	
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for name,value in attrs:
				if name == 'href':
					print value

	def parseanchorlist(self):
		pass
		
if __name__ == '__main__':
	filename = r'D:\PythonStart\windows\www.51voa.com\Development_Report_1.html'
	filecontext = open(filename).read()
	myparser = Parser()
	myparser.init_parser(filename)
	myparser.feed(filecontext)
	print myparser.parseanchorlist()