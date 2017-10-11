#! /usr/local/bin/python3.5


import os, time, cgitb
from http import cookies
cookie = cookies.SimpleCookie()	#initiating cookie object
cookie['lastvisit'] = str(time.time())	# setting up cookie values
cookie['cid'] = str(int(time.time()))
cookie['cid']['expires'] = -1
cookie['name'] = 'Zaheer'

print (cookie)   					# printing cookie to HTTP Header
print ('Content-Type: text/html\n')		
print ('<html><body>')
print ('<p>Server time is', time.asctime(time.localtime()), '</p>')

# The returned cookie is available in the os.environ dictionary
cookie_string = os.environ.get('HTTP_COOKIE')
print (cookie_string)
# The first time the page is run there will be no cookies
if not cookie_string:
    print ('<p>First visit or cookies disabled</p>')

else: # Run the page twice to retrieve the cookie - you don't have to print 
    print ('<p>The returned cookie string was ' + cookie_string + '</p>')  
    # load() parses the cookie string as its complex 
    cookie.load(cookie_string)
    # Use the value attribute of the cookie to get it
    lastvisit = float(cookie['lastvisit'].value)
    cid = str(cookie['cid'].value)
    name = str(cookie['name'].value)
    print ('<p> Hello', name, ' </p>')
    print ('<p>Your last visit was at', time.asctime(time.localtime(lastvisit)), '</p>')
print ('</body></html>')