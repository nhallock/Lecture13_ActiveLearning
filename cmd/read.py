# To solve the driver problem
# uninstall the following
# -----------------------------------
# pip3 uninstall mysql-connector
# -----------------------------------
# Then install
# -----------------------------------
# pip3 install mysql-connector-python
# ----------------------------------- 

import mysql.connector

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password')

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 
cursor = cnx.cursor()
query = ('SELECT * FROM Colleges')
cursor.execute(query)

# print
for row in cursor.fetchall():
    print(row)
cursor.close()
cnx.close()


