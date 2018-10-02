from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.start_preview()
camera.capture('/home/pi/Desktop/image.jpg')
camera.start_recording('haha.h264')
sleep(5)
camera.stop_recording()
