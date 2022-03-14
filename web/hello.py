# import package flask
from flask import Flask

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 
# create flask app
app = Flask(__name__)

# Create route
@app.route("/")
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, port = 3000)