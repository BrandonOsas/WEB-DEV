#! /python34/python
import mysql.connector
 
""" Connect to MySQL database """
conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')
if conn.is_connected():
   print ('Content-type:text/html \n')
   print('<H1> Connected to MySQL database </H1>')
   cursor = conn.cursor()
   cursor.execute("SELECT DEPARTURE FROM pricing")
   row = cursor.fetchone()
   print('<select name="departure">')
   while row is not None:
       print('<option value="',row,'">',row,'</option>')
       row = cursor.fetchone()
   cursor.close()
conn.close()
 
 
