from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.resolution = (1920, 1080) # max for still photo, (2592*1944) for video
camera.framerate = 15

camera.start_preview() # preview only works when a monitor is connected, not for remote access(e.g., ssh) 
# camera.annotate_background = Color('blue')
# camera.annotate_foreground = Color('yellow')
# camera.image_effect = 'colorswap'
# camera.awb_mode = 'sunlight'
# camera.exposure_mode = 'beach'
camera.annotate_text = "RAISE!"
# camera.annotate_text_size = 20
camera.brightness = 70
# camera.contrast = 50
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')

camera.start_recording('haha.h264')
sleep(5)
camera.stop_recording()

camera.stop_preview()

# omxplayer haha.h264
