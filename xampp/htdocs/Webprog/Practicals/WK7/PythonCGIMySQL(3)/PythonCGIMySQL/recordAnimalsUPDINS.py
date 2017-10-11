#! /usr/local/bin/python3.5
import dbfunc, mysql.connector, cgi, cgitb

cgitb.enable()
table  = "animals"
spotted = "spotted"
conn = dbfunc.getConnection()
name = ''
cursor = ''
if conn.is_connected():		
	cursor = conn.cursor()

def selectTable(sqlstat, more):	
	global name
	statement = sqlstat
	cursor.execute(statement, more)
	row = cursor.fetchone()
	name = row[0]
	print ("Animal selected: ", name, "<br />")
	
		
def updateTable(sqlstat, more):
	statement = sqlstat
	cursor.execute(statement, more)
	conn.commit()	
	print('<br> Record: ', more, ' updated')

print ('content-type: text/html \n')
print ('<h1>Animal Selected</h1> <br />')

form = cgi.FieldStorage() 
amount = form.getvalue('amount')
print ("Amount = ", amount, "<br />")

animal_id = form.getvalue('myAnimal')
print ("Animal id = ", animal_id)

sql_statement1 = "SELECT name FROM " + table + " WHERE id = %s"
sql_statement2 = "INSERT INTO spotted (animal, count) VALUES (%s, %s) ON DUPLICATE KEY UPDATE count = (count + %s)"

args1 = (animal_id,)
selectTable(sql_statement1, args1)

args2 = (name, amount, amount)
print("Arguments 2: ", args2)
updateTable(sql_statement2, args2)
cursor.close()
conn.close()