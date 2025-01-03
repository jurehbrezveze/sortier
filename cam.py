import cv2
import time
import numpy as np
class camera:
    def __init__ (self, port, detect2capture_time, remove_top_lines = 120, remove_bottom_lines = 20):
        self.cam_port = port
        self.d2c_time = detect2capture_time
        self.rm_top = remove_top_lines
        self.rm_bot = remove_bottom_lines
    def start(self):
        self.cam = cv2.VideoCapture(self.cam_port, cv2.CAP_DSHOW)
        self.first = 1
    
    def _save_img(self,img):
        cv2.imwrite("part.jpg", img)
    
    def img_as_jpeg(self,img):
        correct_color = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        encode_image = cv2.imencode('part.jpg', correct_color)
        return encode_image[1]
    
    def process(self):
        result, imageOld = self.cam.read()
        #imageOld = imageOld[self.rm_top:-self.rm_bot]
        #imageOld = np.delete(imageOld, np.s_[-], 0)   
        while True :  
            result, image = self.cam.read() 
            #image = image[self.rm_top:-self.rm_bot] #np.delete(image, np.s_[0:100], 0)
            #print(type(image), image)
            
                   
            #print(len(image[0]))
            if result: 
                x =cv2.absdiff(image, imageOld)
                imageOld = image
                change = round(np.average(x))
                print(change)
                cv2.imshow("part", image)
                cv2.waitKey(1)
                if self.first < 30 :
                    self.first = self.first + 1
                else :
                    if change > 8 : 
                        time.sleep(self.d2c_time)
                        image = self.cam.read()[1] 
                        self._save_img(image)     
                        return(image)
                                
            else: 
                print("No image detected. Please! try again") 

