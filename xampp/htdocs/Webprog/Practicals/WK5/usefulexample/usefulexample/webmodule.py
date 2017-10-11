#! /usr/local/bin/python3.5

import cgi, cgitb, re, sys
cgitb.enable() 

#Program logic starts here
print ('Content-type:text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Web Module Page </title>')
print ('</head>')
print ('<body>')
print ("<H1>Web Module Page Contents from a File </H1>")

fh = open('content.txt')  # open file
    
filedata = fh.readlines()   # read all file lines and store in a a list

fh.close()     # close file

print('<table border=1>')     # create table before loop

#loop through filedata list and print items in an HTML table
for row in filedata:
    row = re.split(',', row.rstrip())  #split each item in the row by ',' - now row is a list
    print('<tr>')                      #create table row
    print('<td>', row[0], '</td>')     #create table data - we know from file there are 4 cols 
    print('<td>', row[1], '</td>')
    print('<td>', row[2], '</td>')
    print('<td>', row[3], '</td>')
    print('</tr>')

print('</table>')       # close table after the loop
print('</body>')
print('</html')

