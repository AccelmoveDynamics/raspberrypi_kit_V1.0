import RPi.GPIO as GPIO          #import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False)              #Ignore warning for now
led=18                                            #Set pin 18 to be led
GPIO.setmode(GPIO.BCM)           #Use physical pin numbering
GPIO.setup(led,GPIO.OUT)           #Set  buzzer to be an  output
pwm_led =GPIO.PWM(led,50)        #50Hz pwm frequency
pwm_led.start(100)                            #full brightness,100% Duty Cycle
try:                                                     # run this code
	while True:                            #Run forever
		duty_s= raw_input("Enter Brightness  Value(0 to 100):")
		duty=int(duty_s)                     #convert into interger value
		pwm_led.ChangeDutyCycle(duty)   #function will change the duty cycle after the PWM is started.
		time.sleep(0.5)                            #Sleep for 0.5 second

except:
	GPIO.cleanup()             #Before leaving the try statement 
