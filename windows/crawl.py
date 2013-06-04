#!/usr/bin/env python
# -*- coding: utf-8

from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from urllib import urlretrieve
from urlparse import urlparse, urljoin, urldefrag
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO
from myparser import Parser

class Retriever(object):# download Web pages

	def __init__(self, url):
		self.url = url
		self.file = self.filename(url)

	def filename(self, url, deffile='index.htm'):
		parsedurl = urlparse(url, 'http:', 0) ## parse path
		path = parsedurl[1] + parsedurl[2]
		ext = splitext(parsedurl[2])
		if ext[1] == '': # no file, use default
			if path[-1] == '/':
				path += deffile
			else:
				path += '/' + deffile
		ldir = dirname(path) # local directory
		if sep != '/': # os-indep. path separator
			ldir = replace(ldir, '/', sep)
		if not isdir(ldir): # create archive dir if nec.
			if exists(ldir): 
				unlink(ldir)
			makedirs(ldir)
		return path

	def download(self): # download Web page
		try:
			retval = urlretrieve(self.url, self.file)
		except IOError:
			retval = ('*** ERROR: invalid URL "%s"' %self.url,)
		return retval

	def parseAndGetLinks(self):# parse HTML, save links
		myparser = Parser(self.file)
		return myparser.parseanchorlist()
		
class Crawler(object):# manage entire crawling process

	count = 0# static downloaded page counter

	def __init__(self, url):
		self.q = [url]
		self.seen = ['http://www/51voa.com/Development_Report_1.html']
		print url
		self.dom = urlparse(url)[1]
		print "dom: ", self.dom

	def getPage(self, url):
		r = Retriever(url)
		retval = r.download()
		if retval[0] == '*': # error situation, do not parse
			print retval, '... skipping parse'
			return
		Crawler.count += 1
		print '\n(', Crawler.count, ')'
		print 'URL:', url
		print 'FILE:', retval[0]
		self.seen.append(url)

		links = r.parseAndGetLinks() # get and process links
		print links
		for eachLink in links:
			print eachLink
			if eachLink[:4] != 'http' and \
				find(eachLink, '://') == -1:
				eachLink = urljoin(url, eachLink)
				print '* ', eachLink,
			
			#remove anchor part
			eachLink = urldefrag(eachLink)[0]
			
			if find(lower(eachLink), 'mailto:') != -1:
				print '... discarded, mailto link'
				continue

			if eachLink not in self.seen:
				if urlparse(eachLink)[1] != self.dom:
					print '... discarded, not in domain'
				else:
					if eachLink not in self.q:
						self.q.append(eachLink)
						print '... new, added to Q'
					else:
						print '... discarded, already in Q'
			else:
				print '... discarded, already processed'

	def go(self):# process links in queue
		while self.q:
			url = self.q.pop()
			self.getPage(url)

def main():
	if len(argv) > 1:
		url = argv[1]
	else:
		try:
			url = raw_input('Enter starting URL: ')
		except (KeyboardInterrupt, EOFError):
			url = ''

	if not url:
		return
	robot = Crawler(url)
	robot.go()

if __name__ == '__main__':
	main()
	
##issue list:
##1. why crawl others website context
##2. try to crawl the audio resource in 51voa.com
##3. try to distinct 后缀和文件夹名字