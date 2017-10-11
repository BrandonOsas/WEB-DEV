#! /usr/local/bin/python3.5
import dbfunc, mysql.connector, cgi, cgitb

cgitb.enable()

print ('content-type: text/html \n')
print ('<h1>Animal Selected</h1> <br />')


table  = "animals"
spotted = "spotted"
conn = dbfunc.getConnection()
name = ''
cursor = ''

form = cgi.FieldStorage() 
amount = form.getvalue('amount')
print ("Amount = ", amount, "<br />")

animal_id = form.getvalue('myAnimal')
print ("Animal id = ", animal_id)

if conn.is_connected():		
	cursor = conn.cursor()
	sql_statement1 = "SELECT name FROM " + table + " WHERE id = %s"
	sql_statement2 = "INSERT INTO spotted (animal, count) VALUES (%s, %s)"

	args1 = (animal_id,)

	cursor.execute(sql_statement1, args1)
	row = cursor.fetchone()
	name = row[0]
	print ("Animal selected: ", name, "<br />")	

	args2 = (name, amount)
	print("Arguments 2: ", args2)
	cursor.execute(sql_statement2, args2)
	conn.commit()
	print('<br> Record: ', args2, ' inserted')

	cursor.close()
	conn.close()
else:
	print ('<H2> Error in database connection </H2>')

