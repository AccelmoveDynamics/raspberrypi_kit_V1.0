import RPi.GPIO as GPIO #Libraries
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
r1=23  #set pin 23 to irsensor1  
r2=24 #set pin 24 to irsensor2  
in1=6 #set pin 6 to motordriver in1
in2=5 #set pin 5 to motordriver in1
in3=27 #set pin 27 to motordriver in1
in4=17 #set pin 17 to motordriver in4
ena=19 #set pin 19 to motordriver ENA
enb=4 #set pin 4 to motordriver ENB

GPIO.setup(r1,GPIO.IN) #set r1 to be  an input
GPIO.setup(r2,GPIO.IN) #set r2 to be  an input
GPIO.setup(in1, GPIO.OUT) #set in1 to be  an output
GPIO.setup(in2, GPIO.OUT) #set in2  to be  an output
GPIO.setup(in3, GPIO.OUT) #set in3  to be  an output
GPIO.setup(in4, GPIO.OUT) #set in4  to be  an output
GPIO.setup(ena, GPIO.OUT)  #set ena to be  an output,enable pin is use to control the speed of motor
GPIO.setup(enb, GPIO.OUT) #set enb to be  an output,enable pin is use to control the speed of motor
p=GPIO.PWM(ena,1000)  #50hz frequency
i=GPIO.PWM(enb,1000)  #50hz frequency
p.start(25) #start duty cycle
i.start(25) #start duty cycle
def forward1():  #motor1 rotate forword direction
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
def forward2():#motor2 rotate forword direction
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
def reverse1():   #motor1 rotate reverse direction
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
def reverse2():   #motor2  rotate reverse direction
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
def stop_move():  #stop motor1&2
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
try:
        while True:
                if GPIO.input(r1)==False and GPIO.input(r2)==False:  #ir1 and 2 low
                   forward1()  #motor1 move to be forward
                   print("frd1")
                   p.ChangeDutyCycle(25)  #control speed of motor1
                   forward2()  #motor 2 move to be forward
                   print("frd2")
                   i.ChangeDutyCycle(25) #control speed of motor2
                elif GPIO.input(r1)==False and GPIO.input(r2)==True:  #r1 low and r2 high
                   forward1() #motor1 move to be forward
                   print("frd1")
                   p.ChangeDutyCycle(25)    #control speed of motor1
                   reverse2() #motor2 move to be reverse
                   print("rev2")
                   i.ChangeDutyCycle(25) #control speed of motor2
                elif GPIO.input(r1)==True and GPIO.input(r2)==False:  #r1 high and r2 low
                   forward2()   #motor 2 move to be forward
                   print("frd2") 
                   i.ChangeDutyCycle(25)   #control speed of motor2
                   reverse1()   #motor1 move to be  reverse
                   print("rev1")          
                   p.ChangeDutyCycle(25) #control speed of motor1
                else:
                   stop_move() #motor 1 and 2 stop
                   print("stop")
except:
          GPIO.cleanup()



