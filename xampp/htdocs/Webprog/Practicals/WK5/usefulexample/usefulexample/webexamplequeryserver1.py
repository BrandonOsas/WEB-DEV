#! /usr/local/bin/python3.5

import cgi, cgitb, re, sys
cgitb.enable()

print ('Content-type: text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Web Client Serer Example - Query Responder </title>')
print ('</head>')
print ('<body>')
print ("<H1>Web Technologies ICT2 Preferences Query Results </H1>")

regfile = "example/registration.txt"

data = ''
check = 0

form = cgi.FieldStorage()

keys = list(form.keys())    # get all keys to check if anything is received from the form

if len(keys) > 0:           # To check if there is any form parameter received 
    email = form.getvalue('email')

    fh = open(regfile, "r")
    
    if fh == None:
        print("<H2 style='color:red;'> Unable to open file on server ... ")
        sys.exit()    # quit from program 
    
    if email != None:
        # read all data from file in a list
        filedata = fh.readlines()

        # loop through array to match email
        for row in filedata:
            if re.search(str(email), row, re.IGNORECASE) != None:
                check = 1
                data = row
                break
            else:
                check = 0       

        
        fh.close()
        
        buildoutputstring = ""
        
        if check != None:
            buildoutputstring = "<p>Your registration to Web programming ICT2 has been found:</p>"
            buildoutputstring += "<p>" + data + "</p>"
        
        else:

            buildoutputstring = "<p style='color:#FFFFFF; background:#FF0000;'>Your registration to Web programming ICT2 does not exist - please register again</p>"
            
        testdoc = """           

            <body style="background:#DDFFDD;">
            <h1>Thank you for submitting query!</h1>
            <hr>
            {buildoutputstring}
            <hr>
            </body>
            """

        print (testdoc.format(buildoutputstring=buildoutputstring))
        print('</html>')
        sys.exit()    # quit from program 
    else:
        print("<p style='color:#FFFFFF; background:#FF0000;'>Email shouldn't be empty</p>")

else:
    print("<p style='color:#FFFFFF; background:#FF0000;'>No data received...</p>")
    print('</body>')
    print('</html>')





