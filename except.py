for i in ("asfdasdf", [""]):
	try:
		float(i)
	except ValueError, e:
		print "err", e
	except TypeError, e:
		print "err2", e 
		
		
try:
	assert 1==0, 'assert for 1==0 '
except AssertionError, e:
	print e
