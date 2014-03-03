import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (700, 432)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('/home/pi/img/capture.jpg')

