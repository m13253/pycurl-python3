#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-
# vi:ts=4:et
# $Id: basicfirst.py,v 1.5 2005/02/11 11:09:11 mfx Exp $

import sys
import pycurl

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf

print('Testing', pycurl.version, file=sys.stderr)

try:
    t = Test()
    c = pycurl.Curl()
    c.setopt(c.URL, sys.argv[1])
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.perform()
    c.close()
#    print(t)
    print(t.contents)
except Exception as e:
    print(e)

