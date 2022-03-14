# imports
from flask import Flask, render_template
from flaskext.mysql import MySQL

# web application
app = Flask(__name__)

# connect to db
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MyNewPass'
app.config['MYSQL_DATABASE_DB'] = 'education'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 

