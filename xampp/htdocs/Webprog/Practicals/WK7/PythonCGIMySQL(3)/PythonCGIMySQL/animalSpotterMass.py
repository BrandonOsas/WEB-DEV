#! /usr/local/bin/python3.5
import cgi, cgitb, imp, dbfunc, mysql.connector

cgitb.enable() 
#cgi.test() to test cgi
conn = dbfunc.getConnection()
table  = "animals"

def selectTable(sqlstat, *more):
	statement = sqlstat
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute(statement)
		row = cursor.fetchone()
		print ("<table border=1> <br>")
		while row is not None:
			print ('<tr><td>',row[1],'</td><td><input type="text" name="',row[0],'"</td></tr>')
			row = cursor.fetchone()
		cursor.close()
		print ("</table>")
	conn.close()

print('Content-type: text/html \n')
print ('<H1> Mass Animal Spotter </H1>')
print ("<p>Enter the numbers of animals you have spotted</p>") 
print ('<form method="POST" action="recordAnimalsMass.py">')
sql = 'SELECT * FROM ' + table
selectTable(sql)
print ('<br><input type="submit" value="Submit" /></form><br>')

