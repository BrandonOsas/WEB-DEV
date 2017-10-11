#! /python34/python
import mysql.connector, cgi, cgitb, re, sys, dbfunc
cgitb.enable() 
from datetime import date, datetime, timedelta


print ('Content-type:text/html \n')
conn = dbfunc.getConnection()

# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
keys = list(form.keys())    # get all keys to check if anything is received from the form

flight = form.getvalue('flight_id')
returnflightID = form.getvalue('returnflightid')
tickets = form.getvalue('tickets')




	
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
date = datetime.now()                  ###################Not working need to get date <<<<<<<<<<<<------------------------

if conn.is_connected():		
	cursor = conn.cursor()
	sql_statement1 = "SELECT * FROM `timeanddate` WHERE `flight_id` = %s"
	args1 = [flight.strip()]
	cursor.execute(sql_statement1,args1)
	row = cursor.fetchone()
	currentseats =row[7]
	print("Congratulation you have booked",tickets," tickets to:   ",row[1],"at",row[2],"on",row[3],"to",row[4],"which arrives at",row[5],"for £",row[6],"each","<br /> ")
	#Debugging##############
	#print (cursor.statement)
	#if row is not None:	
	#	print ("<br /><input type='radio' name='flight' value=",row[0],">",row[1],row[2],row[3],row[4],row[5],row[6],"<br />")	
	#Debugging##############

	cursor.close()
if conn.is_connected():		
	cursor = conn.cursor()
	sql_statement2 = "SELECT * FROM `timeanddate` WHERE `flight_id` = %s"
	args2 = [returnflightID.strip()]
	#print(returnflightID)
	cursor.execute(sql_statement2,args2)
	row = cursor.fetchone()
	returncurrentseats =row[7]
	print("Congratulation you have booked",tickets," tickets to:   ",row[1],"at",row[2],"on",row[3],"to",row[4],"which arrives at",row[5],"for £",row[6],"each","<br /> ")
	#Debugging##############
	#print (cursor.statement)
	#if row is not None:	
	#	print ("<br /><input type='radio' name='flight' value=",row[0],">",row[1],row[2],row[3],row[4],row[5],row[6],"<br />")	
	#Debugging##############

	cursor.close()	

if conn.is_connected():	
	cursor = conn.cursor()		
	sql_statement3 = "INSERT INTO `sales`(`FLIGHT_ID`,`returnflightID`,`current_date`,`SEAT`) VALUES (%s,%s,%s,%s)"
	args3 = (flight,returnflightID,date,currentseats,)
	cursor.execute(sql_statement3,args3)
	#Debugging##############
	#print (cursor.statement)
	#Debugging##############

	print ("Your booking id/reference number is:",cursor.lastrowid,"<br /> ")
	print("""<button onclick="myFunction()">Print this page or save a PDF</button>

		<script>
		function myFunction() {
		window.print();
		}	
		</script>""")

	
	cursor.close()
	
if conn.is_connected():
	cursor = conn.cursor()
	sql_statement4 = "UPDATE timeanddate SET seats = %s WHERE Flight_ID = %s "
	newseat = int(currentseats)-int(tickets)
	args4 =(currentseats, flight) 
	cursor.execute(sql_statement4,args4)  
	#Debugging##############
	#print (cursor.statement)
	#Debugging##############	
	conn.commit()    
	cursor.close()	
else:
	print("Sorry there has been an error please contact website admin")
	print("Sorry there has been an error please contact website admin")
	
if conn.is_connected():
	cursor = conn.cursor()
	sql_statement5 = "UPDATE timeanddate SET seats = %s WHERE Flight_ID = %s "
	newseatreturn = int(returncurrentseats)-int(tickets)
	args5 =(returncurrentseats, tickets) 
	cursor.execute(sql_statement3,args3)  
	#Debugging##############
	#print (cursor.statement)
	#Debugging##############	
	conn.commit()    
	cursor.close()	
else:
	print("Sorry there has been an error please contact website admin")
	print("Sorry there has been an error please contact website admin")	
	
conn.close()

print(text2)








                

