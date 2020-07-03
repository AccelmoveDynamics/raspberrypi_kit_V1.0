from bluedot import BlueDot    #Libraries
from gpiozero import Robot
from signal import pause
bd=BlueDot()      #bule dot() set to bd
robot1 = Robot(left=(6,5),right=(27,17))   #set  pins to right and left of motor drive
def move(pos):    #robot moving positions
	if pos.top:   #blue dot drag to top then robot move forword
		robot1.forward()
		print("forward")
	elif pos.bottom:   #blue dot drag to bottom  then robot move backward
		robot1.backward()
		print("backward")
	elif pos.left:    #blue dot drag to left  then robot move left
		robot1.left()
		print("left")
	elif pos.right:   #blue dot drag to right  then robot move right
		robot1.right()
		print("right")
def stop():   #blue dot drag to top then robot move stop
	robot1.stop()
bd.when_pressed=move
bd.when_moved=move
bd.when_released=stop
pause()
