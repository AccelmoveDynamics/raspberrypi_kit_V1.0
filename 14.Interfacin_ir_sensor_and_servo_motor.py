import RPi.GPIO as GPIO   #Libraries
import  time
control=[5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]    #servo rotate positions
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
sensor=17 #ir sensor set to 17 pin
servo=22  # servo set to 22 pin( GPIO 22 pin  isPWM )
GPIO.setup(sensor,GPIO.IN)   # set ir sensor to be  input
GPIO.setup(servo,GPIO.OUT)   # set servo to be  output
GPIO.output(servo,GPIO.LOW)  # servo is off
i=GPIO.PWM(servo,50)  #50hz frequency
i.start(2.5)   #start duty cycle(it set the servo to 0 degree )
try:
	while True:
		if GPIO.input(sensor):   #ir sensor object is detected
			GPIO.output(servo,GPIO.HIGH)    # servo is on
			for x in range(11):   # servo start to rotate
				i.ChangeDutyCycle(control[x])
				time.sleep(0.25)
				print"object detected"
		else:
			print"object not detected"
except:
	GPIO.cleanup()

