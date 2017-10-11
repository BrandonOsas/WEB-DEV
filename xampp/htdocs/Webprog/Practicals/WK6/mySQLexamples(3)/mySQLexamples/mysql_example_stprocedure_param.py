import mysql.connector
 
""" MySQL database and Python """

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='secret')
if conn.is_connected():
  cursor = conn.cursor()
  args = [10,'']
  result_args = cursor.callproc('find_by_id', args)
  print(result_args[0])
  print(result_args[1])   
  cursor.close()

conn.close()
 
 
