import RPi.GPIO as GPIO   #Libraries
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
ir=23    #set ir to 23 pin
in1=6   #set in1 to 6 pin
in2=5  #set in2 to 5 pin
in3=27   #set in3 to 27 pin
in4=17 #set in4  to 17pin
GPIO.setup(ir,GPIO.IN)   #set ir to be input
GPIO.setup(in1, GPIO.OUT)    #set in1 to be output
GPIO.setup(in2, GPIO.OUT)  #set in2 to be output
GPIO.setup(in3, GPIO.OUT)   #set in3  to be output
GPIO.setup(in4, GPIO.OUT)  #set in4 to be output

def forward():  #motar rotate forward 
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
def reverse():    #motar rotate  reverse
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.HIGH)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
try:
	while True:
		if GPIO.input(ir):  #ir sensor object is detected
			print"ir on"
			reverse()   #  motor move reverse 
			print"rev"
		else:       #ir sensor not object is detected
			forward()   #  motor move forward 
			print"frd" 
except:
	GPIO.cleanup()
