import RPi.GPIO as g    #Libraries
import time
g.setmode(g.BCM)  #set GPIO Pins
servo=22   #set GPIO Pins
t=17
e=27
g.setup(servo,g.OUT)  #set GPIO direction (IN / OUT)
g.setup(t,g.OUT)
g.setup(e,g.IN)
p=g.PWM(22,50)
p.start(7.5)
def ping():
	while True:
		g.output(t,g.LOW)     # set Trigger after 0.035ms to LOW
		time.sleep(0.35)
		g.output(t,g.HIGH)  # set Trigger to HIGH
		time.sleep(0.35)
		g.output(t,g.LOW)
		while g.input(e)==0:  # save StartTime
			pulse_start=time.time()
		while g.input(e)==1:  # save time of arrival
			pulse_end=time.time()
		pulse_dur=pulse_end-pulse_start  # time difference between start and arrival
		dis=pulse_dur*17150   # multiply with the sonic speed (17150 cm/s)
		dis=round(dis,2)  # and divide by 2, because there and back
		return dis
try:
	while True:
		if ping()<100:     #distace is less than 100
			print"dis:",ping()
			p.ChangeDutyCycle(2.5)   #servo rotate 0  degree
			time.sleep(1)
			print"0 dgree"
			print"dis:",ping()
			p.ChangeDutyCycle(7.5)   #servo rotate 90  degree
			time.sleep(1)
			print"90 dgree"
		else:
			print"dis:",ping()
			p.ChangeDutyCycle(12.5)   #servo rotate 90  degree
			time.sleep(1)
			print"180 dgree"
except:
	p.stop
	g.cleanup()
