import sys
import gphoto

if 'local' in sys.argv:
    gphoto.capture_local()
else:
    gphoto.capture()