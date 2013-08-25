#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

ids = 33255
weburl = "http://www.1782.cc"
username = "admin1782"
password = "520123"
curl = "C:\Program Files\curl\curl-7.17.1\curl.exe"

command = "%s %d \"%s\" %s %s \"%s\""%(u"dianbo_make.bat ", ids, weburl, username, password, curl)
os.system(command)