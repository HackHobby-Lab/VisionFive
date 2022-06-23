#VisionFive
#This code is used to turn led on and off when button is pressed. And it stays on/off untill button is pressed again.
# It is similar to Button Debounce example on arduino.
import gpiod
chip = gpiod.Chip('gpiochip0')  #gpiochip0 is selected
led2 = chip.get_lines([0])      #gpio pin number '0' or 'GPIO0' or physically pin number '40' of VisionFive is used to connect led.
led2.request(consumer ='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

button = chip.get_lines([2])  #gpio pin number '2' or 'GPIO2' or physically pin number '38' of VisionFive is used to connect button.
button.request(consumer ='foobar', type=gpiod.LINE_REQ_DIR_IN, default_vals=[1])

isPressed = False
isOn = False

while True:
	b = button.get_values() #reading values of GPIO2 will return us with a list
	c= b[0]                 #Since that list contains only one element so no problem with using this for now :)
	print(c)
	if c:
		isPressed = True
	elif isPressed:
		isOn = not isOn
		led2.set_values([isOn])
		isPressed = False

