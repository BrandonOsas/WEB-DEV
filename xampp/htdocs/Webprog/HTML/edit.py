#! /python34/python
import mysql.connector, cgi, cgitb, re, sys, dbfunc
cgitb.enable() 

print ('Content-type:text/html \n')
conn = dbfunc.getConnection()

# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
keys = list(form.keys())    # get all keys to check if anything is received from the form

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
if conn.is_connected():		
	cursor = conn.cursor()
	sql_statement1 = "SELECT * FROM timeanddate"

	#departure = departure.strip( )
	#destination = destination.strip( )
	cursor.execute(sql_statement1)#,departure.strip(),destination.strip())
	print (cursor.statement)
	
	print('<p> #################################################################</p>')
		
	row = cursor.fetchall()
	print ("<form action='update.py'>")
	if row is not None:
		for item in row:
			NewHold = str(item)[2:-3]
			print ("<input type='radio' name='flight_id' value=",item[0],">",NewHold,"<br>")	
			
	else:
		print ("<br />Sorry is no flights")
		
	print ("""<button type="submit">Checkout</button><br />""")	
	
	print ("</form>")


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
