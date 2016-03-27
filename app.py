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

# @app.route('/hello', methods = ['GET', 'POST'])
# def hello():
#      if request.method == 'POST':
#         return "Hello"
#      return 'Hello World'

@app.route('/bullshit', methods = ['POST'])
def bullshit():
    #this method will send a message back to the sender in slack
    #the message will be whatever they sent plus the name of the channel
    #for example /bullshit fuck will return fucknonumber on the channel chat
     #channels.archive('new')

     if request.method == 'POST':
        channelName = request.form.get("channel_name")
        slacker.channels.get_channel_id(channelName)   
        print("hello")
        return request.form.get("text") + channelName 
     return 'Hello World'

     

if __name__ == '__main__':
    app.run(debug=True)