from ms import sorter
import time
s = sorter()

s.start(50)
while 1:
    try:
        time.sleep(0.01)
    except KeyboardInterrupt:
        s.stop()
        exit()
