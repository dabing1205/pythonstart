#!/usr/bin/env python
# -*- coding: utf-8

from bs4 import BeautifulSoup
import formatter

class LinkParser():
	def __init__(self, filename):
		self.filename = filename
		self.linklist = []
	
	def anchorlist(self):
		filecontext = open(self.filename).read()
		soup = BeautifulSoup(filecontext)
		for child in soup.find_all('a'):
			if 'href' in child.attrs:
				self.linklist.append(str(unicode(child['href'])))
		return self.linklist
			
if __name__ == "__main__":
	filename = r"D:\PythonStart\windows\www.51voa.com\VOA_English_Learning\Learn_A_Word_42548.html"
	linkparser = LinkParser(filename)
	print linkparser.anchorlist()