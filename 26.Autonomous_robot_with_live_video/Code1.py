import RPi.GPIO as g  #Libraries
import time
g.setmode(g.BCM)
g.setwarnings(False)
servo=22  #set pin 22 to servo
a=0 #variable a initialize to 0
b=0 #variable b initialize to 0
c=0 #variable c initialize to 0
r1=6 #set right  motor,in1 to be 6
r2=5 #set right  motor,in2 to be 5
l1=27 #set left  motor,in3 to be 27
l2=17 #set left  motor,in4 to be 17
t=18  #set ultrasonic trigger to 18
e=25 #set ultrasonic echo to 25
g.setup(servo,g.OUT) #set servo to be an output
g.setup(r1,g.OUT) #set r1 to be an output
g.setup(r2,g.OUT) #set r2 to be an output
g.setup(l1,g.OUT) #set l1 to be an output
g.setup(l2,g.OUT) #set l2 to be an output
g.setup(t,g.OUT) #set  trigger to be an output
g.setup(e,g.IN) #set echo  to be an input
p=g.PWM(22,50)  #50hz frequency
p.start(7.5)  #start duty cycle(it set the servo to 90 degree )
def ping():
        while True:
                g.output(t,g.LOW) # set Trigger after 0.00001ms to LOW
                time.sleep(0.00001)
                g.output(t,g.HIGH)  # set Trigger after 0.02ms to HIGH
                time.sleep(0.02)
                g.output(t,g.LOW) # set Trigger to LOW
                while g.input(e)==0: # save StartTime
                        pulse_start=time.time()
                while g.input(e)==1: # save time of arrival
                        pulse_end=time.time()
                pulse_dur=pulse_end-pulse_start  # time difference
                dis=pulse_dur*17150  # multiply with sensor speed 
                dis=round(dis,2) # and divide by 2, because there and back
                return dis

def serv0():
        p.ChangeDutyCycle(7.5) #servo rotate 7.5
        a=ping()    #   set ultrasonic sensor distance to variable a 
        print "center= ", a
        time.sleep(1)
        p.ChangeDutyCycle(10)  #servo rotate 10
        b=ping()  #   set ultrasonic sensor distance to variable b
        print "left= " ,b
	time.sleep(1)
        p.ChangeDutyCycle(5)  #servo rotate 5
        c=ping()   #   set ultrasonic sensor distance to variable  c
        print"right= " ,c  
        time.sleep(1)
	p.ChangeDutyCycle(7.5) #servo rotate 7.5
        a=ping()
        print "center= ", a
        time.sleep(1)
        if b>c:  
                left()  #motor move left
                time.sleep(0.5)
                forward()  # motor move forward
        else:  
                right()   #motor move right
                time.sleep(0.5)
                forward()   #motor move forward
def forward():  #motor  move  forward
        print("move forward")
        g.output(r1,g.HIGH)
        g.output(r2,g.LOW)
        g.output(l1,g.HIGH)
        g.output(l2,g.LOW)
def backward():#motor  move  backward
        print("move back")
        g.output(r1,g.LOW)
        g.output(r2,g.HIGH)
        g.output(l1,g.LOW)
        g.output(l2,g.HIGH)

def left():  #motor  move  left
        print("move left")
        g.output(r1,g.HIGH)
        g.output(r2,g.LOW)
        g.output(l1,g.LOW)
        g.output(l2,g.HIGH)
def right():   #motor  move right
        print("move right")
        g.output(r1,g.LOW)
        g.output(r2,g.HIGH)
        g.output(l1,g.HIGH)
        g.output(l2,g.LOW)
def st0p(): #motor stop
        print("stop");
        g.output(r1,g.LOW)
        g.output(r2,g.LOW)
        g.output(l1,g.LOW)
        g.output(l2,g.LOW)
def code():
        if ping()>25:    # distance is greater than 25
                print"dis:",ping()
                forward()   #motor move forward
        if ping()<25:  # distance is less  than 25
                st0p()  #motor stop for 0.2sec
                time.sleep(0.2)
                backward()  #motor go backward for 2 sec
                time.sleep(2)
                st0p()  #motor stop for 0.2 sec
                time.sleep(0.2)
                serv0()   # servo rotate
try:
        while True:   #run forever  
                code()
except:
        p.stop
        g.cleanup()


