#! /python34/python
import mysql.connector, dbfunc
print ('Content-type:text/html \n')

 
""" Connect to MySQL database """
conn = dbfunc.getConnection()

text = """<!DOCTYPE html>
		
		<head>
			<title>index</title>
			<link rel="stylesheet" type="text/css" href="css/default.css">
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
			
			<div class="body">
			"""
print(text)
print("<table>")
print('<tr><td>Depature</td><td>Arrival</td> <td>Price</td></tr>')    
if conn.is_connected():
	   cursor = conn.cursor()
	   cursor.execute("SELECT DEPARTURE, DESTINATION, PRICE FROM pricing")
	   row = cursor.fetchone()
	   while row is not None:
		   print('<tr value="',row,'"><td>',row[0],"</td><td>",row[1],"</td><td>",row[2],'</td></tr>')
		   row = cursor.fetchone()
	   cursor.close()
	   print("</table>")



text2 = """
					
			
				<img src="Plane.png" style="width:304px;height:228px;" align="center">
				
				
				
			</div>
			
				
				
				
		<script src="JavaScript/Javascriptfunctions.js"></script>
			
			
			

		</body>
		</html>"""
print(text2)
