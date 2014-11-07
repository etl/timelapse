import shlex
from subprocess import Popen, PIPE
import re
from time import sleep
import datetime


def cmd(c):
    p = Popen(shlex.split(c), stdout=PIPE, stdin=PIPE, stderr=PIPE)
    std_out, std_err = p.communicate()
    return_code = p.wait()
    # print std_out
    if return_code != 0:
        raise Exception('%s Err=%d >> %s' % (c, return_code, std_err))
    return (return_code, std_out, std_err)


def camera_device():
    list = cmd("lsusb")[1]
    # list = '''Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp.
    # Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    # Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp.
    # Bus 001 Device 004: ID 04a9:3145 Canon, Inc.'''

    for l in list.splitlines():
        print l
        m = re.match('.*?Bus (\d+) Device (\d+).*?Canon', l)
        if m:
            return '/dev/bus/usb/%s/%s' % (m.group(1), m.group(2))


def reset_device():
    dev = camera_device()
    if dev:
        cmd('./usbreset ' + dev)
        print 'reset: ' + dev
    else:
        raise Exception("Device not fount")


def capture():
    reset_device()
    cmd('gphoto2 --set-config capturetarget=1 --capture-image')


def capture_local():
    reset_device()
    cmd('gphoto2 --set-config capturetarget=0 --capture-image-and-download')








