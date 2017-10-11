#! /usr/local/bin/python3.5
import cgi, cgitb, imp, dbfunc, mysql.connector

cgitb.enable() 
#cgi.test() to test cgi
conn = dbfunc.getConnection()

def selectTable(sqlstat):
	statement = sqlstat
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute(statement)
		row = cursor.fetchone()
		print ("<table border=1> <br>")
		while row is not None:
			print ('<tr><td>',row[0],'</td><td>', row[1], '</td></tr>')
			row = cursor.fetchone()
		cursor.close()
		print ("</table>")
	conn.close()

print('Content-type: text/html \n')
print ('<H1> Animal Spotter </H1>')

table  = "animals"
sql = 'SELECT * FROM ' + table
selectTable(sql)
