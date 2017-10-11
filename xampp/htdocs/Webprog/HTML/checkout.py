#! /python34/python
import mysql.connector, cgi, cgitb, re, sys, dbfunc
cgitb.enable() 

print ('Content-type:text/html \n')
conn = dbfunc.getConnection()

# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
keys = list(form.keys())    # get all keys to check if anything is received from the form

table  = "timeanddate"
name = ''
cursor = ''
cprice = 0
Adult = form.getvalue('Adult')
Children = form.getvalue('Children') 
id = form.getvalue('flight')
returnid = form.getvalue('returnflight')


total = 0

Adult = int(Adult)
Children = int(Children)


	
text1 = """<!DOCTYPE html>
                
                <head>
                        <title>index</title>
                        <link rel="stylesheet" type="text/css" href="css/defult.css">
                        <link rel="stylesheet" type="text/css" href="css/index.css">

                        
                </head>
                
                <body>


                        <header>
                                <img src="WEBAIR Logo.png">
                        </header>

                        <nav>
                                <a href="index.py">Home</a>
                                <a href="prices.html">Prices/Flights</a>
                                <a href="account.html">Acount</a>
                                <a href="aboutus.html">About Us</a>
                        </nav>
                         
                        <div class="body">
                                
                                """



text2 = """
                        </div>                          
                <script src="JavaScript/Javascriptfunctions.js"></script>
                        
                        
                        


                </body>
                </html>"""

print(text1)
#print(flight)
print(id[0])


############################## Outbound Flight ############################
if conn.is_connected():         
        cursor = conn.cursor()
        sql_statement1 = "SELECT `leave_airport`,`LEAVE_TIME`,`arrive`,`ARRIVE_TIME`,`Price_ID` FROM `timeanddate` WHERE `Flight_ID` = 	%s"
        arg1 = (id,)
        cursor.execute(sql_statement1, arg1)  
        
        #print (cursor.statement)
        print('<p> #################################################################</p>')
                
        row = cursor.fetchone()
        print ("<form action='confirmation.py'>")

        if row is not None:
                if row is not None:
                        Price = row[4]
                        for item in row:
                                print(item,"<br />")
                                
                                

        if row is None:
                print ("<br />Sorry is no flights")
        cursor.close()
if Adult > 0 and Children > 0:
		cprice = Price * 0.90
		total = (Price * Adult) + (cprice* Children)
			
else:
		total = Price * (Adult + Children) 
print("First flight:",total)

	


############################## Return Flight ############################

if conn.is_connected():         
        cursor = conn.cursor()
        sql_statement2 = "SELECT `leave_airport`,`LEAVE_TIME`,`arrive`,`ARRIVE_TIME`,`Price_ID` FROM `timeanddate` WHERE `Flight_ID` = 	%s"
        arg2 = (returnid,)
        cursor.execute(sql_statement2, arg2)  
        
        #print (cursor.statement)
        print('<p> #################################################################</p>')
                
        row = cursor.fetchone()


        if row is not None:
                if row is not None:
                        returnPrice = row[4]
                        for item in row:
                                print(item,"<br />")
                                
                                

        if row is None:
                print ("<br />Sorry is no flights")
     
if Adult > 0 and Children > 0:
		cprice = returnPrice * 0.90
		totalreturn = (returnPrice * Adult) + (cprice* Children)
		total = total + totalreturn
			
else:
		totalreturn = returnPrice * (Adult + Children)
		total = total + totalreturn
print("return flight price:",totalreturn,"<br />")

print('<p> #################################################################</p>')
	 

	 
	 
print("<br />")
print("Adults:",Adult,"<br />")
print("Children:",Children,"<br />")
print("price of each ticket:",Price,"<br />")
print("price of each ticket:",returnPrice,"<br />")
print ("total price:",total)
print('<p> #################################################################</p>')
tickets = Adult + Children
returntickets = tickets
returnflightid = 0
returnflightid = returnid 
print(returnflightid)
print(id)
print('<input type="hidden" name="flight_id"  value="',id,'">')
print('<input type="hidden" name="returnflightid"  value="',returnflightid,'">')
print('<input type="hidden" name="tickets"  value="',tickets,'">')
print('<input type="hidden" name="returntickets"  value="',returntickets,'">')

print(id)
print(tickets)

print("<br />")




print("The price of each ticket it:",Price,"<br />"," The price of a childs ticket is:",cprice,"<br />"," The total price is:",total)

print ("""<button type="submit">Checkout</button><br />""")	

print("</form>")

print(text2)







                
