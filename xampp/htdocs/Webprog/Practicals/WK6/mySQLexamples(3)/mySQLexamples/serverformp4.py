#! /usr/local/bin/python3.5
import cgi, cgitb, sys, mysql.connector

cgitb.enable()  # to enable browser to show errors 

form = cgi.FieldStorage() 		# receives all form data sent by client and saves in a dictionary (key, value pairs)
id_param = form.getvalue('id')	# get value of 'id' field sent by client form

conn = mysql.connector.connect(user='root', 
							   password='secret', 
							   host='localhost', 
							   database='webprog')
if conn.is_connected():
  cursor = conn.cursor()
  args = [id_param,'']  		# build args with all data you want to send to SQL statements
  result_args = cursor.callproc('find_by_id', args)  # calls stored procedure and passes arguments/parameters
  cursor.close()
conn.close()

print('Content-Type: text/html \n')
print ("<h1>Animal ID </h1>", result_args[0], ". <h1>Animal Name</h1> ", result_args[1], ". <br />")
print ("</body>")
print ("</html>")
 
