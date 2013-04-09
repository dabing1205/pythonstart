import os
f = open('log.txt', 'r')
count = 0
for line in f:
	count += 1
	print repr(line),
f.close()
print count

f1 = open('writelog.txt' , 'w')
while True:
	aline = raw_input("enter log: ")
	if aline != '.':
		f1.write('%s%s'%(aline, os.linesep))
	else:
		break

f1.close()