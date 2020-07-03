import RPi.GPIO as GPIO        #import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False)           #Ignore warning for now        
GPIO.setmode(GPIO.BCM)      #Use physical pin numbering
GPIO.setup(18,GPIO.OUT)      #Set  pin 18 to be an  output pin
GPIO.output(18,GPIO.HIGH)   # Turn  on
print("led on")
time.sleep(1)                #Sleep for 1 second
