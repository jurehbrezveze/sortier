import requests
import ms
import json
import cv2
import time
import numpy
from cam import camera
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

def main():
    try:
        m = ms.sorter()
        m.start(40)
        c = camera(0,0.5)
        c.start()
        img = c.process()
        id = brickognise(img)
        print(id)
        cv2.imshow("pic", img)
        cv2.waitKey(100)
        m.stop()
        exit
       
    finally:
        m.stop()

main()