import picamera      #Libraries
import time

camera = picamera.PiCamera()   #camera on
camera.vflip = True     #image get vertical flip
camera.capture('example.jpg')   #image capture and save in example.jpg

