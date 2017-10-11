#! /usr/local/bin/python3

import cgi, cgitb, re
cgitb.enable() 

#Program logic starts here
print ('Content-type: text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Web Client Server File Search Example </title>')
print ('</head>')
print ('<body>')
print ("<H1>Search Text Example </H1>")


# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
searchString = form.getvalue('search')   # get search variable 
print("<br><H2 style='color:red;'> Search String: ", searchString)
fh = open("test2_animals.txt")
fhdatalist = fh.readlines()

for line in fhdatalist:
	line = line.rstrip()
	if re.search(str(searchString), line) != None:
		print ('<br>Line Found: ', line)

fh.close()
print('</body>')
print('/html>')
