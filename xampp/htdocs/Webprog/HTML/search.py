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

departure = form.getvalue('DEPARTURE') 
destination = form.getvalue('DESTINATION') 
departuredate = form.getvalue('departuredate') 
returndate = form.getvalue('returndate') 
Adult = form.getvalue('Adult') 
Children = form.getvalue('Children') 
departuredate = form.getvalue('departuredate')
returndate = form.getvalue('returndate')


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
print('<p>',departure,'</p>')
print('<p>',destination,'</p>')
print('<p>',departuredate,'</p>')
print('<p>',returndate,'</p>')
print('<p>',Adult,'</p>')
print('<p>',Children,'</p>')



                


		######Outbound Flight#######################

if conn.is_connected():         
        cursor = conn.cursor()
        sql_statement1 = "SELECT * FROM `timeanddate` WHERE `leave_airport` = %s and `arrive` = %s and leave_date = %s"	  #Outbound
        sql_statement2 = "SELECT * FROM `timeanddate` WHERE `leave_airport` = %s and `arrive` = %s and leave_date = %s"   #return 

        args1 = [departure.strip(), destination.strip(), departuredate.strip()]	#Outbound
        cursor.execute(sql_statement1,departure.strip(),destination.strip())
        cursor.execute(sql_statement1,args1)
        #Debugging##############
        #print (cursor.statement)
        #Debugging##############
        print('<p> #################################################################</p>')
        row = cursor.fetchall()
        i = 0
        print ("<form action='checkout.py'>") 
        print ("<fieldset id='group1'>") 
        if row is not None:     
                for item in row:
                        print ("<input type='radio' name='flight' value=",row[i][0]," name=`group1`>",row[i][1],row[i][2],row[i][3],row[i][4],row[i][5],row[i][6],"<br>")    ######Change back to radio 
                        i = i + 1
       
    
        else:
                print ("<br />Sorry is no flights please check the dates and the airports")
        print ("</fieldset>")
		
		######Return Flight#######################
		
        args2   = [destination.strip(),departure.strip(), returndate.strip()] #return
        cursor.execute(sql_statement2,args2)
        #Debugging##############
        #print (cursor.statement)
        #Debugging###############
        print('<p> #################################################################</p>')
        row = cursor.fetchall()
        i = 0
        print ("<form action='checkout.py'>") 
        print ("<fieldset id='group2'>") 
        if row is not None:     
                for item in row:
                        print ("<input type='radio' name='returnflight' value=",row[i][0],"name=`group2`>",row[i][1],row[i][2],row[i][3],row[i][4],row[i][5],row[i][6],"<br>")  ######Change back to radio    
                        i = i + 1
      

        #else:
               # print ("<br />Sorry is no flights please check the dates and the airports")
                print ("</fieldset>") 
        print('<p>Adults',Adult,'</p>')
        print('<p>Children',Children,'</p>')
        print('<input type="hidden" name="Adult"  value="',Adult,'">')
        print('<input type="hidden" name="Children"  value="',Children,'">')    
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
