# Printing Lists as Tabular Data
# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

# Console colors - rick pythong package
# https://github.com/willmcgugan/rich

# Markdown tables - Github syntax
# https://docs.github.com/en/github/writing-on-github/organizing-information-with-tables

import mysql.connector
from tabulate import tabulate

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='',
    auth_plugin='mysql_native_password')

cursor = cnx.cursor()
query = ("SHOW DATABASES")
cursor.execute(query)

# print all the first cell of all the rows
# for row in cursor.fetchall():
#     print(row)

# example
# print(tabulate(myresult, headers=['EmpName', 'EmpSalary'], tablefmt='psql'))

# get column names
field_names = [i[0] for i in cursor.description]

# get query result
result = cursor.fetchall()

# print using tabulate
print(tabulate(result, headers=field_names,tablefmt='psql'))

cursor.close()
cnx.close()
