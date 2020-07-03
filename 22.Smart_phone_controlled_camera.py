from bluedot import BlueDot   #Libraries
from picamera import PiCamera
from signal import pause
bd=BlueDot()  #set bluedot to bd
cam=PiCamera()   #set picam to cam
def take_picture():  #image capture
	cam.capture("pic.jpg")
bd.when_pressed=take_picture   #blue dot is press then take image
pause()
