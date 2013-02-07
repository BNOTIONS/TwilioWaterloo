from twilio.rest import TwilioRestClient

twilio_key = 'YOUR_API_KEY'
twilio_secret = 'YOUR_API_SECRET'
client = TwilioRestClient(twilio_key, twilio_secret)

to_number = raw_input("Enter your phone number:\n")
from_number = 'YOUR_TWILIO_NUMBER'

twiml = 'URL_TO_A_TWIMLET'

client.calls.create(to=to_number, from_=from_number, url=twiml)

print "Calling now..."
