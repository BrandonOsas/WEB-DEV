#! /usr/local/bin/python3.5
import cgi, cgitb, mysql.connector, imp

# MYSQL CONFIG VARIABLES
host           = "localhost";
db             = "webprog";
user           = "root";
passwd         = "secret"

def getConnection():
	conn = mysql.connector.connect(user=user,
								   password=passwd,
								   host=host,
								   database=db)
	return conn
