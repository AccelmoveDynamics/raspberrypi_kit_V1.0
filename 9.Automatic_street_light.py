import RPi.GPIO as g  #import Raspberry Pi GPIO library
import time
g.setmode(g.BCM)  #Use physical pin numbering
g.setwarnings(False)   #Ignore warning for now
ldr=23                        #Set pin 23 to be ldr
led=24                       #Set pin 24 to be led
g.setup(led,g.OUT)  #led to be an  output
try:           # run this code
	while True:   #Run forever
		g.setup(ldr,g.OUT)     #set ldr to be an  output
		g.output(ldr,g.LOW)   # ldr is turn  off
		time.sleep(0.1)      #Sleep for 0.1 second
		diff =0     # time difference set to 0
		g.setup(ldr,g.IN)    #set ldr to be an  input
		currenttime=time.time()  #set current time
		while(g.input(ldr)==g.LOW):  #ldr in put value is low
			diff=time.time()-currenttime  #calculate the time differance
		value=diff*1000  #difference is multiple with 1000
		print(value)
		time.sleep(1)  #Sleep for 1 second
		if value< 1000:
			print("led off") 
			g.output(led,False)  #led off
		else:
			print("led on")
			g.output(led,True)  # led on
except:
	g.cleanup()   #Before leaving the try statement
