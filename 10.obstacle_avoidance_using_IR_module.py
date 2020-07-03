import RPi.GPIO as GPIO          #import Raspberry Pi GPIO library
import  time  
GPIO.setwarnings(False)            #Ignore warning for now  
GPIO.setmode(GPIO.BCM)        #Use physical pin numbering
sensor=17                                    #Set pin 17 to be sensor
led=27                                          #Set pin 27 to be led
GPIO.setup(sensor,GPIO.IN)      #set ldr to be an  input
GPIO.setup(led,GPIO.OUT)      #set led to be output
GPIO.output(led,False)              #led off
print("IR sensor redy")	
try:                                             # run this code
	while True:          #Run forever
		if GPIO.input(sensor):              #object is detected
			GPIO.output(led,True)   #led on
			print"object detected"  		  
		else:
			GPIO.output(led,False)    #led off
			print"object not detected"
except:
	GPIO.cleanup()        #Before leaving the try statement
