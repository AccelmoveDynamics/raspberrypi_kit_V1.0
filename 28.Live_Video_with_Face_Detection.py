#import  packages
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
#capture frames from the camera
for  frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
        image = frame.array        #Load a cascade file for detecting faces
        face_cascade = cv2.CascadeClassifier('/home/pi/accelmove/faces_file/face.xml')
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #Convert to grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Look for faces in the image using the loaded cascade file
        for (x,y,w,h) in faces:   #Draw a rectangle around every found face
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)  #face detected
        image = frame.array
        cv2.imshow("Frame",image)  #show the frame
        key = cv2.waitKey(1)
        rawCapture.truncate(0)
        if key == ord("q"):
                break

