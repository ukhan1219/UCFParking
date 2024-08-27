from pyicloud import PyiCloudService
import sys
import os
from dotevn import load_dotenv

load_dotenv()
IPHONE_KEY = os.getenv('IPHONE_KEY')
api = PyiCloudService('#########@gmail.com', '##########')


if __name__ == "__main__":
    if api.requires_2fa:
        print ("Two-factor authentication required.")
        code = input("Enter the code you received of one of your approved devices: ")
        result = api.validate_2fa_code(code)
        print("Code validation result: %s" % result)

        if not result:
            print("Failed to verify security code")
            sys.exit(1)

        if not api.is_trusted_session:
            print("Session is not trusted. Requesting trust...")
            result = api.trust_session()
            print("Session trust result %s" % result)

            if not result:
                print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
iphone1 = api.devices[IPHONE_KEY]
print (api.devices[4])
print (api.devices[4].location())
# print (api.iphone.location())
# api.iphone.play_sound()

#ucf coordinates lat 28.597658, long -81.208000