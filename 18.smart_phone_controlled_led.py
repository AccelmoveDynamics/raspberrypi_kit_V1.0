#Libraries
from bluedot import BlueDot
from gpiozero import LED

bd=BlueDot() #set bd to bluedot
led = LED(18)  # set pin 18 to be led
while True:
	bd.wait_for_press()
	print("led on")      #press bluedot app then led is on
	led.on()
	bd.wait_for_release()     # release bluedot app then led is on
	led.off()
	print("led off")

