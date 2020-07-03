import RPi.GPIO as GPIO            #import Raspberry Pi GPIO library
import time
led1=18                                         #Set pin 18 to be led1
led2=17                                         #Set pin 17 to be led1
led3=27                                         #Set pin 27 to be led1
GPIO.setwarnings(False)             #Ignore warning for now
GPIO.setmode(GPIO.BCM)        #Use physical pin numbering
GPIO.setup(led1,GPIO.OUT)     #Set  led1 to be an  output 
GPIO.setup(led2,GPIO.OUT)      #Set  led2to be an  output 
GPIO.setup(led3,GPIO.OUT)      #Set  led3 to be an  output 

try:                 #run this code

	while True:          #Run forever
		GPIO.output(led1,GPIO.HIGH)   # led1 is turn  on
		time.sleep(0.5)       #Sleep for 0.5 second
		print("led1:on")
		GPIO.output(led1,GPIO.LOW) # led1  is turn  off
		time.sleep(0.5) #Sleep for 0.5 second
		print("led1:off")
		GPIO.output(led2,GPIO.HIGH) # led2 is turn  on
		time.sleep(0.5) #Sleep for 0.5 second
		print("led2:on")
		GPIO.output(led2,GPIO.LOW) # led2 is turn  off
		time.sleep(0.5)  #Sleep for 0.5 second
		print("led2:off")
		GPIO.output(led3,GPIO.HIGH)    # led3 is turn  on
		time.sleep(0.5)     #Sleep for 0.5 second
		print("led3:on")
		GPIO.output(led3,GPIO.LOW)    # led3 is turn  off
		time.sleep(0.5)     #Sleep for 0.5 second
		print("led3:off")

except:
	GPIO.cleanup()    #Before leaving the try statement
