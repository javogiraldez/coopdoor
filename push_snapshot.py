#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from pushbullet import Pushbullet
from picamera import PiCamera
import sys
import time
import ConfigParser
import subprocess

def takepic():
        camera = PiCamera()
        camera.start_preview()
        time.sleep(5)
        camera.capture('/tmp/coop.jpg')
        camera.stop_preview()

if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read('/opt/coopdoor/coopdoor.cfg')
    api_key = config.get('DEFAULT', 'pushbullet_api_key')
    pb = Pushbullet(api_key)

    try:
        cmd = takepic()
        subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        with open("/tmp/coop.jpg", "rb") as pic:
            file_data = pb.upload_file(pic, "coop.jpg")
        push = pb.push_file(**file_data)

    except:
        print "BOOM:", sys.exc_info()
