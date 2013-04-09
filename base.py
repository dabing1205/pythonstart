import sys
import testmodule

#print raw_input('Enter something : ') 

def somefunction():
	'''Test doc function
	Test doc function.'''
	pass

print somefunction.__doc__ 
print 'The PYTHONPATH is', sys.path
print testmodule.version
testmodule.sayhi()
testmodule.version = 0.4
print testmodule.version
testmodule.sayhi()
print 'dir(testmodule)',dir(testmodule)
print testmodule.__file__