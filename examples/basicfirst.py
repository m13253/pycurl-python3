# $Id: basicfirst.py,v 1.1 2002/08/16 16:23:06 kjetilja Exp $

import sys
import pycurl

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf

print 'Testing', pycurl.version

t = Test()
c = pycurl.Curl()
c.setopt(c.URL, 'http://curl.haxx.se/dev/')
c.setopt(c.WRITEFUNCTION, t.body_callback)
c.setopt(c.HTTPHEADER, ["I-am-a-silly-programmer: yes indeed you are",
                        "User-Agent: Python interface for libcURL"])
c.perform()
c.close()

print t.contents