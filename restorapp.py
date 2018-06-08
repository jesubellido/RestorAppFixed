# Import necessary things.
from flask import Flask, render_template, request, Response, session, jsonify
from model import entities
from database import connector
import json
import xml

# Initializes app.
app = Flask(__name__, static_url_path="/static", static_folder='static')

# I'll create an object from the manager class from the connector file,
# which will in turn create a database called 'db'.
db = connector.Manager()

# Create cache
cache = {}

# Create a database engine.
engine = db.create_engine()

@app.route('/')
def hello_world():
    return render_template('welcome.html')


@app.route('/signUp')
def sign_up():
    return render_template('signup.html')

@app.route('/logIn')
def log_in():
    return render_template('login.html')

#This makes the app actually run:
if __name__ == '__main__':
    app.run()
