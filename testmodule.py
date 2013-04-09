def sayhi():
	global version
	print 'Hi, this is mymodule speaking.'
	print 'module version:' , version

version = '0.1'

if __name__ == '__main__':
	print "run by myself"
	print version
# End of mymodule.py