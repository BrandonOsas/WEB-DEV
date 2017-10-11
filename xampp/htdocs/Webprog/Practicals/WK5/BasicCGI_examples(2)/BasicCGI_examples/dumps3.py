#! /usr/local/bin/python3.5
import cgi, cgitb

cgitb.enable() 
form = cgi.FieldStorage() 
keys = list(form.keys())
print('Content-type: text/html \n')
print ('<H1> Data Dump </H1>')
print('<H2>')
for key in keys:
	print (key, " : ", form.getvalue(key), "</br>")
print('</H2>')

