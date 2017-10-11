#! /usr/local/bin/python3.5

import cgi, cgitb, re   # Import modules for CGI handling 
cgitb.enable()			# for error trace

print ("Content-type:text/html \n")
print ("<HTML>")
print ("<HEAD>")
print ("<TITLE>Serverside - File processing</TITLE>")
print ("</HEAD>")
print ("<BODY>")

form = cgi.FieldStorage() # Create instance of FieldStorage 

findstring = form.getvalue('find')			# Get data from form fields
replacestring  = form.getvalue('replace')

print ('<b>Search string = </b>', findstring)
print ('<br> <b>Replace string </b> = ', replacestring)
print ('<br><br>')

# Open text file in read mode
fhr = open('test2_animals.txt','r')
fhw = open('test2_animals_copy.txt', 'w')

if fhr != None and fhw != None:		# checking - files are opened
	print ("<H2> Both files have been opened ... </H2><br>")
else:
	print ("Error while opening file ...<br>")

print ("<H1>Searching File .... test2_animals.txt </H1><br>")

count = 1		#counter for line numbers 

filedatalist = fhr.readlines()		# read all file lines in a list

for line in filedatalist:	# loop through each line search, print and write
	line = line.rstrip()	
	if re.search(findstring, line) != None:	# search and print
		print('<br>Line # : ', count, ' = ', line)
		count += 1
	else:
		count += 1

	newline = re.sub(findstring, replacestring, line)   #find and replace
	newline = newline+'\n'
	fhw.write(newline) 	

fhr.close()
fhw.close()

print('<br><H1>Printing lines from new file .... test2_animals_copy.txt </H1')
count = 1
fh = open('test2_animals_copy.txt', 'r')
filedatalist = fh.readlines()

for line in filedatalist:
	line = line.rstrip()
	if re.search(replacestring, line) != None:	# search and print
		print('<br>Line # : ', count, ' = ', line)
		count += 1
	else:
		count += 1

print ("</BODY>")
print ("</HTML>")


