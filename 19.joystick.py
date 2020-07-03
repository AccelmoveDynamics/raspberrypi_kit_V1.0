#Libraries
from bluedot import BlueDot
from signal import pause
def dpad(pos):  # it was pressed to go up, down, left, right like the D-pad on a joystick
	if pos.top:
		print("up")
	elif pos.bottom:
		print("down")
	elif pos.left:
		print("left")
	elif pos.right:
		print("right")
	elif pos.middle:
		print("fire")
bd = BlueDot()   #set bd to bluedot
bd.when_pressed = dpad    # d pad only registers whem it is pressed
pause()

