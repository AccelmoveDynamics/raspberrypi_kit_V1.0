import RPi.GPIO as GPIO#import raspberry pi GPIO library
import time

GPIO.setmode(GPIO.BCM)#use physical pin numbering

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO27
GPIO.setup(18, GPIO.OUT)  #LED to GPIO18

try: #run this code
    while True:
         button_state = GPIO.input(27) 
         if button_state == False: #button is pressed
             GPIO.output(18, True) #led on
             print('Button Pressed...')
             time.sleep(0.2)
         else:
             GPIO.output(18, False) #led off
             print('Button not pressed')
except:
    GPIO.cleanup()
