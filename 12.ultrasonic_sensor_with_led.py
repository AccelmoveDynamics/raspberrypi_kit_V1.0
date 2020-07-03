#Libraries
import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
#set GPIO Pins
TRIGER =17
ECHO =27
GREEN=18
RED=23
#set GPIO direction (IN / OUT)
GPIO.setup(TRIGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
def green():
	GPIO.output(GREEN,GPIO.HIGH) #green led on
	GPIO.output(RED,GPIO.LOW) #red led off
def red():
	GPIO.output(GREEN,GPIO.LOW)  #green led off
	GPIO.output(RED,GPIO.HIGH)    #red led off
def distance():
	GPIO.output(TRIGER, False)   # set Trigger after 0.00001ms to LOW
	time.sleep(0.00001)
	GPIO.output(TRIGER, True)    # set Trigger to HIGH

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
			dist = distance()
			print ("Measured Distance = %.1f cm" % dist)
			time.sleep(0.25)
			if  dist >=500:
				green()
				print("green led on")
			else:
				red()
				print("red led on")
	# Reset by pressing CTRL + C
	except:
		GPIO.cleanup()
