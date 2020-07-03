#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
#set GPIO Pins
TRIGER =17
ECHO = 27
 
#set GPIO direction (IN / OUT)
GPIO.setup(TRIGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
 
def distance():
	GPIO.output(TRIGER, False) # set Trigger after 0.00001ms to LOW
	time.sleep(0.00001)
	GPIO.output(TRIGER, True)
    
 
    # save StartTime
	while GPIO.input(ECHO) == 0:
		StartTime = time.time()
 
    # save time of arrival
	while GPIO.input(ECHO) == 1:
		StopTime = time.time()
	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300) / 2
	return distance
 
if __name__ == '__main__':
	try:
		while True:
			dist = distance() #measure distance for each 0.25 sec
			print ("Measured Distance = %.1f cm" % dist)
			time.sleep(0.25)
 
        # Reset by pressing CTRL + C

	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()


