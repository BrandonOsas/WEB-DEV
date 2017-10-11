#! /usr/local/bin/python3.5
import cgi, cgitb, sys, mysql.connector

cgitb.enable()  #to enable browser to show errors 

form = cgi.FieldStorage() 
id_param = form.getvalue('id')

conn = mysql.connector.connect(user='root', 
							   password='Hangten10', 
							   host='localhost', 
							   database='webprog')
if conn.is_connected():
  cursor = conn.cursor()
  args = [id_param,'']  
  result_args = cursor.callproc('find_by_id', args)  
  cursor.close()
conn.close()

print('Content-Type: text/html \n')
print ("<h1>Animal ID </h1>", result_args[0], ". <h1>Animal Name</h1> ", result_args[1], ". <br />")
print ("</body>")
print ("</html>")
 
