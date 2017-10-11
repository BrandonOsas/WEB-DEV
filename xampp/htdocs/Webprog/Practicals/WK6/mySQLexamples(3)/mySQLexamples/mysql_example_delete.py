import mysql.connector
 
""" MySQL database and Python """

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='secret')
if conn.is_connected():
  print('Connected to MySQL database')
  cursor = conn.cursor()
  
  query =  "DELETE FROM animals WHERE id = %s"

  animal_id = 16
  args = (animal_id,)
  
  cursor.execute(query,args)  
  conn.commit()    
  cursor.close()

conn.close()
 
 
