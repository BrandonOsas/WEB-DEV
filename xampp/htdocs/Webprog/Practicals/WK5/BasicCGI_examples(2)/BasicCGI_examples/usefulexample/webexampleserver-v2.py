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


# Following function is defined to check if all form parameters are received in correct format
def ok():
    okey = 1
    if name == None:
        print ("<p style='color:red;'>Your name is required!</p>") 
        okey = 0

    if email == None:
        print ("<p style='color:red;'>Your E-mail address is required!</p>")
        okey = 0
    elif re.search(r"@",email) == None:
        print ("<p style='color:red;'>An E-mail address must contain the @ </p>")
        okey = 0
    if webtech == None:
        print ("<p style='color:red;'>Test preferences is required!</p>")
        okey = 0
    if okey == 0:
        print ("<p style='color:red;'>Please enter missing data and resubmit</p>")    
    return okey

# Following funciton is defined to display error page
def failpage():
    print ("<title>Error page</title>")
    print ("<p>Error: cannot record your registration for ICT2 - File handling error for file : ", regfile, "</p>")
    sys.exit()

# Following function is defined to show form again to get new data
def reloadpage():
    print ("<H3 style='color:red;'>Try again - Please register your interest or preference for In-Class Test 2</H3>")
    
    again = """
        <Form action="webexampleserver.py" method="get">
            <H2>ICT2 Registration</H2>
            <p>Name : <input type="text" name="name"> </p>
            <p>Email :<input type="text" name="email"></p>
            <br /> <H3>Web Technologies ICT2 Preferences (select one):</H3> <input type="hidden" name="hide">
                
            <input type="radio" name="webtech" value="HTML css"> HTML and CSS <br/>
            <input type="radio" name="webtech" value="Python program" checked> HTML and Perl CGI <br/>
            <input type="radio" name="webtech" value="Java script"> JavaScript and HTML <br/>
            <input type="radio" name="webtech" value="None"> Need more practice - will try in ICT3 <br/>
                
            <p>Submit button:</p>
            <input type=submit value="Register">
                
        </Form>
    """
    print (again)

# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
keys = list(form.keys())    # get all keys to check if anything is received from the form

if len(keys) > 0:           # To check if there is any form parameter received 
    name = form.getvalue('name')    # To get name value 
    email = form.getvalue('email')  # To get email value 
    webtech = form.getvalue('webtech')  # To get webtech value
    
    if ok():                # ok() funciton is called to check if all form parameters are correct  
        fh = open(regfile,"a")      # Open file in append mode
        if fh == None:              # If error in opening file then call failpage() and exit
            failpage()
            sys.exit()

        #you can replace "\t" with ", " to create csv file
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
        reloadpage()
else:
    print("<H3 style='color:red;'> No form parameters received</H3>")
