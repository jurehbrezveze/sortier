import requests
from oauthlib.oauth1 import Client
import urllib.parse
import json

base_url = "https://api.bricklink.com/api/store/v1/items/part/"

consumer_key = "10CBEEC750144F168292873208A2B103"
consumer_secret = "ACA56412A1914EFDA7598BFBC20B7E79" 
token_key = "15C1D234E13D445F8FAB64ED8CD4625C" 
token_secret = "2E21F4660F0244ADAFE0606C2520E5EC" 


client = Client(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=token_key,
    resource_owner_secret=token_secret,
    signature_method='HMAC-SHA1',
)


def getItem(part_number):
    encoded_part_number = urllib.parse.quote(part_number)
    url = f"{base_url}{encoded_part_number}"

    #print(f"Request URL: {url}")

    uri, headers, body = client.sign(url)

    # Make the GET request
    response = requests.get(uri, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and print the entire response JSON
        data = response.json()
        #print(f"Response for Part Number: {part_number}")
        #print(data)
        return(data)
    else:
        print(f"Failed to fetch data for part number: {part_number}. Status code: {response.status_code}, Response: {response.text}")
        print(f"OAuth Headers: {headers}")
        return 0
    
#print(getItem("98283"))

'''
f = open("part.json", "w")
x = getItem("98283")
a = json.dumps(x, indent=4)
f.write(a)
f.close()
'''
