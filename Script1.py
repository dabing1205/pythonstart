#encording=utf-8

import os
import string
import re


f = open("bugzilla.txt","r")
bugstring = f.read()
#print string
bugformat = re.compile(r"(importance)")
'''match = bugformat.match(bugstring)
if match:
    print "matched", match.group(1)
'''
match = re.search('<td>(P[1-5])(\s*)(\w*)(\s)', bugstring)
if match:
    print "matched"
    print match.group(1),match.group(3)
print "helloworld "