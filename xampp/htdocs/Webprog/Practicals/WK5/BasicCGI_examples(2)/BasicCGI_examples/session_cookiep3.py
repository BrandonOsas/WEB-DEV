#! /usr/local/bin/python3.5

import time, os, cgitb # /usr/local/bin/python3.5
from http import cookies
cgitb.enable()      # for debugging - errors shown in webpages
cookie = cookies.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')

# If new session
if not cookie_string:
    # The cid will be based on the server time
    cid = str(int(time.time()))      
    cookie['lastvisit'] = str(time.time())  # cookie properties
    cookie['cid'] = cid
    cookie['cid']['expires'] = 12 * 30 * 24 * 60 * 60
    cookie['name'] = 'Zaheer'
# If already existent session
else:
    cookie.load(cookie_string)
    cid = cookie['cid'].value
print (cookie)
print ('Content-Type: text/html')
print()
print ('<html><body>')
print ('Hello World')
if cookie_string:
    print ('<p>Already existent session</p>')
else:
    print ('<p>New session</p>')
print ('<p>SID =', cid, '</p>')
print ('</body></html>')