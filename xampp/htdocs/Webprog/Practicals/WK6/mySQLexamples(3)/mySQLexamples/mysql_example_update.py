import mysql.connector
 
""" MySQL database and Python """

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='secret')
if conn.is_connected():
  print('Connected to MySQL database')
  cursor = conn.cursor()
  query = """ UPDATE animals
              SET name = %s
              WHERE id = %s """
  (name, animal_id) = ('Snake', 14)
  args = (name, animal_id)

  cursor.execute(query,args)  
  conn.commit()    
  cursor.close()

conn.close()
 
 
