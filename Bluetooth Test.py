#VisionFive
'''This python script will be using bluetooth module of visionfive board and will be communicating
to android device. We will be able to control the gpio pins after running this script.
'''

import bluetooth
import gpiod
chip = gpiod.Chip('gpiochip0')  #gpiochip0 is selected
led2 = chip.get_lines([0])      #gpio pin number '0' or 'GPIO0' or physically pin number '40' of VisionFive is used to connect led.
led2.request(consumer ='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print("accepted connection from", address)
while 1:
    data = client_socket.recv(1024)
    cmd = data.decode("utf-8")
    if cmd == 'ON':
        led2.set_values([1])
    elif cmd == 'OFF':
        led2.set_values([0])
    
        
    
