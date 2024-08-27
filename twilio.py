from twilio.rest import Client
import os
from twilio.twiml.voice_response import VoiceResponse, Say
from flask import Flask, render_template, request 
from dotenv import load_dotenv

load_dotenv()

TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')
TWILIO_SECRET_KEY = os.getenv('TWILIO_SECRET_KEY')



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# client = TwilioRestClient(account_sid, auth_token)

# call = client.calls.create(
#                         url='http://demo.twilio.com/docs/voice.xml',
#                         to='+##############',
#                         from_='+##############'
#                     )

# print(call.sid)


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+##############"
TWILIO_PHONE_NUMBER = "+############"

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+############"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://twimlets.com/echo?Twiml=%3CResponse%3E%0A%3CSay%20voice%3D"

# https://handler.twilio.com/twiml/EH8a7af905ac184baddf241d9266058302
# https://hookb.in/DrllGOoKR2sPajxxaRWR
# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = Client(TWILIO_API_KEY, TWILIO_SECRET_KEY)


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        response = VoiceResponse()
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps

        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")
    

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.xml')

if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)
    app.run(debug=True)
    


#PORT FORWARD NIGGER