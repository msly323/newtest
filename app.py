from flask import Flask, request, redirect, session
import twilio.twiml
from slacker import Slacker
import json 

# Makes use of a secret key
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)
slack = Slacker('xoxp-28038241029-28038195079-28266163220-166a67df32')
#print(slack.channels.get_channel_id('new'))
#slack.channels.create("new3")
#slack.channels.unarchive("new2")

unArch = slack.channels.get_channel_id('new')
infoArch = slack.channels.info(unArch)
jsonInfo = json.dumps(infoArch.body)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/bullshit', methods = ['POST'])
def bullshit():
    #this method will send a message back to the sender in slack
    #the message will be whatever they sent plus the name of the channel
    #for example /bullshit fuck will return fucknonumber on the channel chat
     #channels.archive('new')

     if request.method == 'POST':
        channelName = request.form.get("channel_name")
        # 
        
        # print(channelName)
        # #slacker.channels.info(channelName)
        # print(slack.channels.get_channel_id('general'))
        # print(slack.channels.get_channel_id('new'))
        # genID = slack.channels.get_channel_id('general')
        # newID = slack.channels.get_channel_id('new')

        #new code

        unArch = slack.channels.get_channel_id('new')
        infoArch = slack.channels.info(unArch)
        jsonInfo = json.dumps(infoArch.body)
        # parsedJson = json.loads(jsonInfo)
        # print(parsedJson['channel']['is_archived'])

        #new code 


       # newID = slack.channels.get_channel_id('new3')
        #print(newID)
       # slack.channels.unarchive(newID)
        return request.form.get("text") + channelName 
     return 'Hello World'

     

if __name__ == '__main__':
    app.run(debug=True)   