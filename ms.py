from mindstorms import Hub
from mindstorms import Motor
import time
def kuza(hub):
    tone = 1000
    for j in range(2):
        for i in range (4):
            hub.sound.beep(tone, 100)
            time.sleep(0.3)
        tone = tone+100   
    for j in range(2):
        hub.sound.beep(tone, 100)
        time.sleep(0.3)
        tone = tone - 100
    for j in range(2):       
        hub.sound.beep(tone, 100)
        time.sleep(0.3)
    tone = tone - 100
    for j in range(3):
        hub.sound.beep(tone, 100)
        time.sleep(0.3)

class sorter:
    def __init__(self):
        self.hub = Hub()
        self.belt1 = self.hub.port.E.motor 
        self.belt2 = self.hub.port.F.motor 
        time.sleep(0.7)   #required for hub to start working
    def start(self, speed):        
        self.belt2.run_at_speed(-speed*0.7)
        self.belt1.run_at_speed(-speed*1.5)
    def stop(self):        
        self.belt1.brake()
        self.belt2.brake()
        
#s = sorter()
#s.start(50)
#time.sleep(2)
#s.stop()
