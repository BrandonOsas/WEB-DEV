#! /usr/local/bin/python3.5
import cgi, cgitb
import sys
import os

cgitb.enable() 
form = cgi.FieldStorage() 
keys = list(form.keys())

print('Content-type: text/html \n')
print ('<H1> Data Dump </H1>')
print ('data items: ', len(keys), '</br>')
print('<H2>')
for key in keys:
	print (key, " : ", form.getvalue(key), "</br>")
print('</H2>')

"""
#print all system environment variables
for en, val in os.environ.items():
  print (en, val, " </br>")

print ("<h2> System lib Path </h2>")
print (sys.path)
"""
