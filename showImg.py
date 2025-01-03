import cv2
import json
import numpy as np
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def img(url):
    req = requests.get(f'http:{url}',headers=headers)

    if req.status_code == 200:
        arr = np.asarray(bytearray(req.content), dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)
        
        if img is not None:
            cv2.imshow('showImg', img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Error decoding the image.")
    else:
        print(f"Error fetching the image: {req.status_code}")