import RPi.GPIO  as  GPIO    #Libraries
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
in1=6  #set 6 pin to in1
in2=5   #set 5 pin to in2
in3=27   #set 27 pin to in3
in4=17 #set 17 pin to in4
GPIO.setup(in1, GPIO.OUT)  #set in1 to be an out put
GPIO.setup(in2, GPIO.OUT) #set in2  to be an out put
GPIO.setup(in3, GPIO.OUT)   #set in3  to be an out put 
GPIO.setup(in4, GPIO.OUT)   #set in4  to be an out put
def forward():   #motor rotate in forward direction
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
	time.sleep(3)
def reverse():     #motor rotate in reverse direction
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.HIGH)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
	time.sleep(3)
try:
	while True:
		forward()    #forward function 
		print"frd"
		reverse()   #reverse function
		print"rev"
except:
	GPIO.cleanup()
