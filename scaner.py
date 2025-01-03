import cv2
import brickogniseAPI as b
from scanCam import camera
import base
import fancy

path = 1

def main():

    while True:
        c = camera(0,0.5)
        c.start()
        img = c.process()
        id = b.brickognise(img)
        print(id)
        cv2.imshow("pic", img)
        fancy.show(str(id))
        #base.insert(id,path)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows() 

main()