# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
import signal

# Find these values at https://twilio.com/user/account
account_sid = "AC733d141e59351adbab06d66eb8253347"
auth_token = "0019a7152652c5176f9fd3f8d7f91f40"
client = TwilioRestClient(account_sid, auth_token)


n = 100

def inbound_message(n): 
    print("hello")
    if n==0:
        return 0
    else:     
        signal.alarm(20) 
        message = client.messages.create(to="+18448168960", from_="+14246662592",
                                     body="Hello there!")
        return inbound_message(n-1)


inbound_message(n)

