#import  the necessary packages 
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
#initialize the camera and grab a referance to the raw camera capture
camera = PiCamera()
camera.resolution =(640,480)
camera.framerate=32
rawCapture = PiRGBArray(camera,size=(640,480))
#allow the camera to warmup
time.sleep(0.1)
for  frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
        image = frame.array
        #show the frame
        cv2.imshow("Frame",image)
        key = cv2.waitKey(1)
        #clear the stream in preparation for the next frame 
        rawCapture.truncate(0)
        #if the q key  was pressed,break from the loop
        if key == ord("q"):
                break
