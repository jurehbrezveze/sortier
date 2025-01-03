import requests
import json

def brickognise(img):
    url = 'https://api.brickognize.com/predict/parts/'
    files = {'query_image': ('part.jpg', open('part.jpg','rb'), 'image/jpeg')}
    headers= {'accept': 'application/json'} 
    x = requests.post(
        url,
        headers=headers,
        files=files,
    )
    json_object = json.loads(x.text)
    json_formatted_str = json.dumps(json_object["items"][0]['id'] , indent=2)
    print(json_formatted_str)
    return json_formatted_str