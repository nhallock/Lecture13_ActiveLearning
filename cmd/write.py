import mysql.connector

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password')

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 
college = input('Enter college name')
students = input('Enter student population')
cursor = cnx.cursor()
query = (f'INSERT INTO `Colleges` VALUES NULL, {college}","{students}", NULL, NULL, NULL)')

cursor.execute(query)

query = ('SELECT * FROM Colleges')
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cnx.commit()
cursor.close()
cnx.close()

