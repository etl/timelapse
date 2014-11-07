import datetime
from time import sleep
import gphoto

while True:
    print "shot " + str(datetime.datetime.now()) + " >"
    try:
        gphoto.capture()
    except Exception as e:
        print e

    sleep(70)

