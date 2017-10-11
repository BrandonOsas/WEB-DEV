import cgi, cgitb, imp, dbfunc, mysql.connector
from mysql.connector import Error

cgitb.enable()	# for error checking
#cgi.test() to test cgi

conn = dbfunc.getConnection()	# to create database connection - you don't need this here - guess why?

def connect():
	""" Connect to MySQL database """
	try:
		conn = mysql.connector.connect(host='localhost',
                                       database='webprog',
                                       user='root',
                                       password='secret')
		if conn.is_connected():
			print('Connected to MySQL database')
			cursor = conn.cursor()
			cursor.execute("CREATE TABLE temp (TempId int, Role varchar(255), ChangeDate varchar(20))")
	except Error as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
    connect()
