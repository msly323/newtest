from flask import Flask, request, redirect, session
import twilio.twiml
from slacker import Slacker

# Makes use of a secret key
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

    
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello', methods = ['GET', 'POST'])
def hello():
     if request.method == 'POST':
        return "Hello"
     return 'Hello World'

@app.route('/bullshit', methods = ['POST'])
def bullshit():
     if request.method == 'POST':
        return request.POST['username']
     return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)