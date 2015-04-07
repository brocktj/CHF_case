__author__ = 'brock'
from twilio.rest import TwilioRestClient

auth_token1 = '279cccc1aeabd147eec2a179902f9cb0'
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC1d871be38b07534bc9b26312e2eaaa3d"
auth_token  = auth_token1
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Oh hey Jacob, this is a message sent from within my django app, it's pretty legit right?",
    to="+17024960232",    # Replace with your phone number
    from_="+12086293984") # Replace with your Twilio number
print(message.sid)