#! /usr/local/bin/python3.5
import cgi, cgitb, imp, dbfunc, mysql.connector

cgitb.enable() 
#cgi.test() to test cgi
conn = dbfunc.getConnection()

def selectTable(sqlstat, *more):
	statement = sqlstat
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute(statement)
		row = cursor.fetchone()
		print ("<table border=1> <br>")
		while row is not None:
			print ('<tr><td><input type="radio" name="myAnimal" value=', row[0], '></td><td>', row[1], '</td></tr>')
			row = cursor.fetchone()
		cursor.close()
		print ("</table>")
	conn.close()

print('Content-type: text/html \n')
print ('<H1> Animal Spotter Update </H1>')

table  = "animals"
print ('<form method="POST" action="recordAnimalsUPD.py">')
sql = 'SELECT * FROM ' + table
selectTable(sql)
print ('<br>How many have you seen? <input type="text" name="amount"/><br>')
print ('<br><input type="submit" value="Submit" /></form><br>')

