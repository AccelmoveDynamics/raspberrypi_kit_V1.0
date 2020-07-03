import RPi.GPIO as GPIO         #import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False)           #Ignore warning for now
GPIO.setmode(GPIO.BCM)     #Use physical pin numbering
buzzer=18                                 #Set pin 18 to be buzzer
GPIO.setup(buzzer,GPIO.OUT)    #Set  buzzer to be an  output
try:                     # run this code
	while True:     #Run forever
		GPIO.output(buzzer,GPIO.HIGH)   # buzzer is turn  on
		print ("Beep")
		time.sleep(2)   #Sleep for 2 second
		GPIO.output(buzzer,GPIO.LOW)   # buzzer is turn  off
		print ("No Beep")
		time.sleep(0.5)   #Sleep for 0.5 second
except:
	GPIO.cleanup()    #Before leaving the try statement 
