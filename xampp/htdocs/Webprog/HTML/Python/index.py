#! /python34/python
import mysql.connector, dbfunc
print ('Content-type:text/html \n')

 
""" Connect to MySQL database """
conn = dbfunc.getConnection()

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
				<a href="index.html">Home</a>
				<a href="prices.html">Prices/Flights</a>
				<a href="account.html">Acount</a>
				<a href="aboutus.html">About Us</a>
			</nav>

			<div class="booking">
				<p> Booking </p>
				
				<form action="search.py">
					<p>Leave - At - Arrive - At</p>"""
print(text)
def getData (Name):
	if conn.is_connected():
	   cursor = conn.cursor()
	   cursor.execute("SELECT Name FROM pricing")
	   row = cursor.fetchone()
	   print('<select name="Name">')
	   while row is not None:
		   print('<option value="',row,'">',row,'</option>')
		   row = cursor.fetchone()
	   print('</select>')
	   cursor.close()
	else:
		print("Not Connected")

name1 =("DEPARTURE")
name2= ("DESTINATION")
getData = (name1)
getData = (name2)



text2 = """
					<br><br>
					<p>Departure - Return</p>
					
					<input type="date" name="departuredate">
					<input type="date" name="returndate">

					<p>Adult - Children </p>
					<input type="number" name="Adult" min="0" max="5">
					<input type="number" name="Children" min="0" max="5">
					<br>
					<p>Children from age 0-9. Children flying alone will be charge adult fair.</p>
				
					
					<br><br>
					
					
					<input type="submit">
				</form>
				
			</div>
			<div class="body">
				<img src="Plane.png" style="width:304px;height:228px;" align="center">
				
				
				
			</div>
			
				
				
				
		<script src="JavaScript/Javascriptfunctions.js"></script>
			
			
			

		</body>
		</html>"""
print(text2)
