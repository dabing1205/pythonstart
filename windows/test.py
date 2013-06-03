#!/usr/bin/env python
# -*- coding: utf-8

import HTMLParser
import urllib

file = 'develop.html'
retval = urllib.urlretrieve('http://www.51voa.com/Development_Report_1.html', file)
print retval