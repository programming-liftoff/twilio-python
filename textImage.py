from twilio.rest import Client

account_sid = '' # Found on Twilio Console Dashboard
auth_token = '' # Found on Twilio Console Dashboard

myPhone = '' # Phone number you used to verify your Twilio account
TwilioNumber = '' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)
client.messages.create(
  to=myPhone,
  from_=TwilioNumber,
  media_url='https://raw.githubusercontent.com/programming-liftoff/twilio-python/master/python.png')
