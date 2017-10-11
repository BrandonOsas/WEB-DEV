#! /usr/local/bin/python3.5

import cgi, cgitb
cgitb.enable() 
  
print('content-type: text/html \n')
 
fh = open ('hotel.html','rt', encoding='latin1')
for line in fh:
	print(line)


  
