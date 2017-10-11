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




text = """<!DOCTYPE html>
		
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
#departure.strip()
print(text)



		



if conn.is_connected():
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM `timeanddate`")
   rows = cursor.fetchall()
   print('Total Row(s):', cursor.rowcount,"<br />")
   for row in rows:
       print(row,"<br />") 
   cursor.close()
conn.close()
 
 




print(text2)
cursor.close()
conn.close()




		####### Key for row ######
		# fligh_ID = row[0]		
		# leave_airport = row[1]	
		# leave_time = row[2]	
		# arrive = row[3]	
		# arrive_time = row[4]	
		# price = row[4]	
