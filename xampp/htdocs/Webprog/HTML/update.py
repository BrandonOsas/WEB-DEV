#! /python34/python
import mysql.connector, cgi, cgitb, re, sys, dbfunc
cgitb.enable() 

print ('Content-type:text/html \n')
conn = dbfunc.getConnection()
Flight_ID = 3#form.getvalue('flight_id')
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
        </html>
        """



        


print(text1)
def update(Flight_ID, leave_airport, LEAVE, LEAVE_TIME, arrive, ARRIVE_TIME, Price_ID, id):
        if conn.is_connected():
            cursor = conn.cursor()
            query = """ UPDATE timeanddate
                    SET Flight_ID = %s, leave_airport = %s, LEAVE-TIME = %s, arrive = %s, ARRIVE-TIME = %s, Price_ID = %s
                    WHERE id = %s """
            args = (Flight_ID, leave_airport, LEAVE-TIME, arrive, ARRIVE-TIME, Price_ID, id)
            cursor.execute(query,args)  
            conn.commit()    
            cursor.close()
        conn.close()
        return;


if conn.is_connected():     
    cursor = conn.cursor()
    sql_statement1 = "SELECT * FROM timeanddate where Flight_ID = 3"


    cursor.execute(sql_statement1)#Flight_ID.strip())
    print (cursor.statement)
    
    print('<p> #################################################################</p>')
        
    
        
    row = cursor.fetchone()
    print ("<form action='update(row[0], row[1], row[2], row[3], row[4], row[5], Flight_ID)'>")
    if row is not None:
            print ("<input type='number' name='flight_id' value =", row[0],">",row[0],"<br>")
            print ("<input type='text' name='leave_airport' value =", row[1],">",row[1],"<br>")
            print ("<input type='time' name='leave_time' value =", row[2],">",row[2],"<br>")
            print ("<input type='text' name='arrive_airport' value =", row[3],">",row[3],"<br>")
            print ("<input type='time' name='arrive_time' value =", row[4],">",row[4],"<br>")
            print ("<input type='number' name='price' value =", row[5],">",row[5],"<br>")
            
    else:
        print ("<br />Sorry is no flights")
        
    print ("""<button type="submit">Update</button><br />""")   
    
    print ("</form>")


print(text2)





