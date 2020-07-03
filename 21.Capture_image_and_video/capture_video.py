import picamera    #Libraries
import time
camera = picamera.PiCamera()   #camera on
camera.vflip = True   #video get vertical flip
camera.start_recording('examplevid.h264')   #recording start
time.sleep(5)    #5 sec vido
camera.stop_recording    # stop recordng

