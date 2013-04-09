import os
def input():
	print '''
	1. sum five numbers
	2. avg five numbers
	3. exit
	'''
	return int(raw_input("input: "))
	
while(1):
	command = "cls"
	os.system(command)

	inputvalue = input()
	if inputvalue == 1:
		print "summmmm five"
	elif inputvalue == 2:
		print "avggggg five"
	else:
		break;