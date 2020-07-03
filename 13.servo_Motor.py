import RPi.GPIO as GPIO  #Libraries
import time

GPIO.setmode(GPIO.BCM)
servo=22   #set servo is pin 22
GPIO.setup(servo,GPIO.OUT)
i=GPIO.PWM(servo,50) #50hz frequency
i.start(2.5) #start duty cycle(it set the servo to 0 degree )
try:
	while True:
		i.ChangeDutyCycle(2.5) #servo rotate 0 degree
		print("0 degree")
		time.sleep(1)
		i.ChangeDutyCycle(7.5)   #servo rotate 90 degree
		print("90 degree")
		time.sleep(1)
		i.ChangeDutyCycle(12.5)   #servo rotate 180 degree
		print("180 degree")
		time.sleep(1)

except:
	GPIO.cleanup()

