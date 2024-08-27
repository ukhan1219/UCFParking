import requests

url = 'https://hookb.in/DrllGOoKR2sPajxxaRWR'

data = {
    "name": "John"
}

r = requests.post(url, verify=False, json=data)