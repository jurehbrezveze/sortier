import brickAPI
import showImg

def show(id):
    x = brickAPI.getItem(id)
    print(x)
    data = x["data"]

    showImg.img(data["image_url"])
