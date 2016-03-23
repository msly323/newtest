from flask import Flask, request, redirect, session
import twilio.twiml
from slacker import Slacker

# Makes use of a secret key
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

callers = {
    '+14246662592': 'Nick'
}

slack = Slacker('xoxp-28038241029-28038195079-28266163220-166a67df32')

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    from_number = request.values.get('From', None)

    # if from_number in callers:
    #     message = callers[from_number] + ", thanks for the message!"
    # else:
    #     message = "Monkey, thanks for the message!"


    # ####
    # if from_number is None:
    #     user_channel = '#noNumber'
    # else:
    #     user_channel = '#' + from_number

    # slack.channels.join(user_channel)

    # slack.chat.post_message('#general', 'Hello fellow slackers!')
   # slack.chat.post_message('#general', from_number)
    #slack.chat.post_message(user_channel, 'Hello fellow slackers!')

    ###

    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
 
    return str(resp)


#    resp = twilio.twiml.Response()
   # resp.message(message)

 #   return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
