#! /usr/local/bin/python3.5

import cgi, cgitb, re, sys
cgitb.enable() 

#Program logic starts here
print ('Content-type:text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Web Client Server Example </title>')
print ('</head>')
print ('<body>')
print ("<H1>Web Technologies ICT2 Preferences </H1>")

# To test cgi
#cgi.test()

regfile = "example/registration.txt"
name = ''
email = ''
webtech = ''
filestring = ''

# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
keys = list(form.keys())    # get all keys to check if anything is received from the form

if len(keys) > 0:           # To check if there is any form parameter received 
    name = form.getvalue('name')    # To get name value 
    email = form.getvalue('email')  # To get email value 
    webtech = form.getvalue('webtech')  # To get webtech value
    
    fh = open(regfile,"a")      # Open file in append mode
    if fh == None:              # If error in opening file then call failpage() and exit
        print("<H2 style='color:red;'> Unable to open file on server ... ")
        sys.exit()

    #you can replace "\t" with ", " to create csv file
    if name != None or email != None: 
        filestring =  name + "\t" + email + "\t" + webtech + "\n"
        fh.write(filestring)
    fh.close()
        
    # Construct useful/meaningful message on the webpage
    testdoc = """
            <title>Thank you!</title>
            <body style="background:#DDFFDD;">
            <h1>Thank you!</h1>
            <p>Your registration to Web programming ICT2 has been recorded as follows:</p>
            <p>Name: {name}</p>
            <p>E-mail: {email}</p>
            <p>ICT preference: {webtech}</p>
            </body>
            """

    print(testdoc.format(name=name, email=email, webtech=webtech))   
    print("<br/><br/>")

    # Displaying registration list in a one column table
    print("<H2>Registration List</H2>")
    fh = open(regfile)
    print("<table border='1'>")
    print("<th>Name, Email, Technology</th>")
    for line in fh:
        print("<tr><td>")
        print(line.rstrip())
        print("</td></tr>")            
    print("</table>")     
    #sys.exit()
    print("Go back to <a href='webexampleclient.html'>Registraion Form</a>")    

else:
    print("<H3 style='color:red;'> No form parameters received</H3>")
    print("Go back to <a href='webexampleclient.html'>Registraion Form</a>")