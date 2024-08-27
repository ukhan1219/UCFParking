import urllib.request
from twilio.rest import TwilioRestClient
import sys,tweepy,smtplib, time, datetime
from email.message import EmailMessage
import urllib.parse
import re
import os
from dotenv import load_dotenv
load_dotenv()

TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')
TWILIO_SECRET_KEY = os.getenv('TWILIO_SECRET_KEY')

url = 'https://secure.parking.ucf.edu/GarageCount/'
values = {}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print (respData)

paragraphs = re.findall(r'<strong>(''.*?'')</strong>', str(respData))

garage = []


for eachT in paragraphs:
    garage.append(eachT)
    print (garage)
garage.pop()
print (garage)

for i in range(0, len(garage)):
    garage[i] = int(garage[i])

class Garage:
    def __init__(self, availableSpaces, totalSpaces):
        self.availableSpaces = availableSpaces
        self.totalSpaces = totalSpaces
        # percentEmpty = (self.availableSpaces/self.totalSpaces)*100
        self.percentEmpty = round(((int(availableSpaces)/int(totalSpaces))*100), 2)
        

gA = Garage(garage[0], '1623')
gB = Garage(garage[1], '1259')
gC = Garage(garage[2], '1852')
gD = Garage(garage[3], '1241')
gH = Garage(garage[4], '1284')
gI = Garage(garage[5], '1231')
gLibra = Garage(garage[6], '1007')

# gB = Garage(garage[1], '1259', round(((garage[1]/int('1259'))*100), 2))
# gC = Garage(garage[2], '1852', ((garage[2]/int('1852'))*100))
# gD = Garage(garage[3], '1241', ((garage[3]/int('1241'))*100))
# gH = Garage(garage[4], '1284', ((garage[4]/int('1284'))*100))
# gI = Garage(garage[5], '1231', ((garage[5]/int('1231'))*100))
# gLibra = Garage(garage[6], '1007', ((garage[6]/int('1007'))*100))

print (gA.availableSpaces, gA.totalSpaces, gA.percentEmpty)
GList = [gA, gB, gC, gD, gH, gI, gLibra]
for i in range(0, len(GList)):
    Garage.inform(i)



# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+########"
TWILIO_PHONE_NUMBER = "+#########"

# list of one or more phone numbers to dial, in "+###########" format
DIAL_NUMBERS = ["+############"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient(TWILIO_API_KEY, TWILIO_SECRET_KEY)


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)