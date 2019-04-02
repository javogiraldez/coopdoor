#!/usr/bin/python
#import RPi.GPIO as GPIO
import time
import datetime
import ConfigParser
from pushbullet import Pushbullet
from picamera import PiCamera

fileName = "/tmp/coop.jpg"

def takepic():
	camera = PiCamera(resolution=(1920, 1200), framerate=30)
	camera.iso = 800
	camera.vflip = True
	camera.hflip = True
	# Turn the camera's LED on
	camera.led = True
	camera.start_preview()
	# Camera warm-up time
	time.sleep(5)
	# Now fix the values
	camera.shutter_speed = camera.exposure_speed
	camera.exposure_mode = 'off'
	g = camera.awb_gains
	camera.awb_mode = 'off'
	camera.awb_gains = g
	camera.shutter_speed = 6000000
	camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	time.sleep(20)
	camera.capture(fileName)
	camera.stop_preview()

def send_notification(api_key, message):
	pb = Pushbullet(api_key)
	my_channel = pb.channels[0]
	pushN = my_channel.push_note('CoopDoor', message)
	#pb.push_note('Chicken Door', message)
	with open(fileName, "rb") as pic:
	    file_data = pb.upload_file(pic, "coop.jpg", file_type="image/jpeg")
	pushF = my_channel.push_file(**file_data)

if __name__ == '__main__':
	config = ConfigParser.ConfigParser()
	config.read('/opt/coopdoor/coopdoor.cfg')
	#config.read('coopdoor.cfg') #for local testing
	api_key = config.get('DEFAULT', 'pushbullet_api_key')

	try:
		takepic()
		time.sleep(2)
		#resp = "testing this" #placeholder for message for testing
		send_notification(api_key, message)
	except:
		print "BOOM:", sys.exc_info()
