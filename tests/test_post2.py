# $Id: test_post2.py,v 1.4 2002/08/08 12:03:55 kjetilja Exp $

import pycurl

pf = ['field1=this is a test using httppost & stuff', 'field2=value2']

c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.sourceforge.net/tests/testpostvars.php')
c.setopt(c.POST, 1)
c.setopt(c.HTTPPOST, pf)
c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
