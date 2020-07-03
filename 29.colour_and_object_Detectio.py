# import the necessary packages
import cv2      
import numpy as np 
from picamera.array import PiRGBArray
from picamera import PiCamera
def nothing(x):
        pass 
#create the trackbars to help us with selecting a color 
cv2.namedWindow("Trackbars")
cv2.createTrackbar("B", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("G", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("R", "Trackbars", 0, 255, nothing)
#we set the resolution at (640,480)and the frame rate at 30fps
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480)) 
#capture continuos unction to start reading the frames from the raspberry pi camera module.
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        #now we are going to convert images from the bgr to hsv color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #we create the trackbars used to select the color
        B = cv2.getTrackbarPos("B", "Trackbars")
        G = cv2.getTrackbarPos("G", "Trackbars")
        R = cv2.getTrackbarPos("R", "Trackbars")

        #we can find out the lower and upper limit of color in  hsv
        green = np.uint8([[[B, G, R]]])
        hsvGreen = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
        lowerLimit = np.uint8([hsvGreen[0][0][0]-10,100,100])
        upperLimit = np.uint8([hsvGreen[0][0][0]+10,255,255])
        #we adjust the threshold of the hsv image for a range of each selected colour
        mask = cv2.inRange(hsv, lowerLimit, upperLimit)
        #now we can extract the object of the colors in the frame
        result = cv2.bitwise_and(image, image, mask=mask)
        #letâ€™s show the result in the output  window 
        cv2.imshow("frame", image)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)
        key = cv2.waitKey(1)        #always clear the stream in preparation for the next frame by calling truncate(0) between captures.
        rawCapture.truncate(0)
        if key == 27:
                break
cv2.destroyAllWindows()
