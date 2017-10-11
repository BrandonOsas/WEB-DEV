#! /usr/local/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
name = form.getvalue('name')
module  = form.getvalue('module')

print ("Content-type:text/html\n")
print ("<HTML>")
print ("<HEAD>")
print ("<TITLE>Hello - Form processing</TITLE>")
print ("</HEAD>")
print ("<BODY>")
print ("<H1>Hello ", name, " You're enrolled to study ", module, ". Enjoy!</H1>")
print ("</BODY>")
print ("</HTML>")

