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
        <body background="Sky.jpg">
        </body>
		
		<body>


			<header>
				<img src="WEBAIR Logo V2.png">
					<div id="loginbox">       
			
			</div>	
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

if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT AIRPORTS FROM airports")
            row = cursor.fetchall()
            print('<select name="DEPARTURE">')
            if row is not None:
                for item in row:
                    NewHold = str(item)[2:-3]
                    Newhold = NewHold.replace(' ', '')

                    print('<option value="',NewHold,'">',NewHold,'</option>')
                    #row = cursor.fetchone()
            print('</select>')
            cursor.close()
			
if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT AIRPORTS FROM airports")
            row = cursor.fetchall()
            print('<select name="DESTINATION">')
            if row is not None:
                for item in row:
                    NewHold = str(item)[2:-3]
                    print('<option value="',NewHold,'">',NewHold,'</option>')
		   #row = cursor.fetchone()
            print('</select>')
            cursor.close()
	   

text2 = """
				<script> 
				document.getElementById('checkbox').onchange = function() {
				document.getElementById('returndate').enabled = this.checked;};

				</script>
				<br><br>
					<p>Departure - Return</p>
					<p>Departure - Return</p>
					<p>Departure - Return</p>
					<input type="checkbox" name="return" id = "checkbox" action="EnableTextbox(checkbox,returndate)"value="true"> Would you like to return<br>

					<input type="date" name="departuredate">
					<input type="date" id = "returndate" name="returndate">

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
