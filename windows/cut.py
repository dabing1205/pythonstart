#!/usr/bin/env python

import sys
import os
import re

filename = sys.argv[1]
filename_new = filename + '.bk'
f = open(filename_new, 'w')
[f.write(j) for j in [re.sub(r'\d+ ?', '', i) for i in file(filename, 'r') ]]
f.close()
command = "mv %s %s"%(filename_new, filename)
os.system(command)
