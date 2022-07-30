from bocadillo import App, Templates, static
from aiohttp import web
import socketio
import VisionFive.gpio as GPIO
from time import *
import psutil
import re

temp = psutil.sensors_temperatures()

led= 0
led1= 1
led2= 2
led3= 3
led4= 4
led5= 8
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.output(led5, GPIO.HIGH)
p= GPIO.PWM(led5, 100)
p.start(0)

client_count = 0


sio = socketio.AsyncServer()

app = web.Application()
## Binds our Socket.IO server to our Web App
## instance
sio.attach(app)


@sio.event
async def connect(sid, environ):
    global client_count
    client_count += 1
    print(sid, 'connected')
    await sio.emit('client_count', client_count)

@sio.event
async def disconnect(sid):
    global client_count
    client_count -= 1
    print(sid, 'disconnected')
    await sio.emit('client_count', client_count)


@sio.on('Temperature')
async def temperature(sid, Temperature):
    temp = psutil.sensors_temperatures()
    data = str(temp['124a0000.tmon'])
    words = data.split()
    dab = words[1]
    feww = float(re.search("\d+\.\d",dab).group())
    neww = (f'{feww} C')
    await sio.emit('Temperature', neww)
    print("Temperature Requested")
    
    


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('message')
async def print_message(sid, message):
    await sio.emit('message', message)
    print("Socket ID: " , sid)
    print(message)
     
@sio.on('pwm')
async def print_pwm(sid, pwm):
    await sio.emit('pwm', pwm)
    p.ChangeDutyRatio(int(pwm))
    print(pwm)

@sio.on('message')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    print(message)
##ONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

    if message == "LIGHTs":
        
        GPIO.output(led, GPIO.HIGH)
    if message == "DOORs":
        GPIO.output(led1, GPIO.HIGH)       
    if message == "FANs":
        GPIO.output(led2, GPIO.HIGH)
    if message == "ACs":
        GPIO.output(led3, GPIO.HIGH)
    if message == "DSKTOs":
        GPIO.output(led4, GPIO.HIGH)

##OFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF    

    if message == "LIGHTsoff":
        GPIO.output(led, GPIO.LOW)
    if message == "DOORsoff":
        GPIO.output(led1, GPIO.LOW)
    if message == "FANsoff":
        GPIO.output(led2, GPIO.LOW)
    if message == "ACsoff":
        GPIO.output(led3, GPIO.LOW)
    if message == "DSKTOsoff":
        GPIO.output(led4, GPIO.LOW) 

               
    ## await a successful emit of our reversed message
    ## back to the client
    #temp = psutil.sensors_temperatures()
    #data = str(temp['124a0000.tmon'])
    #words = data.split()
    #dab = words[1]
    #feww = float(re.search("\d+\.\d",dab).group())
    #neww = (int(feww) )
    await sio.emit('message', message)
    #await sio.emit('message', neww)
    

## We bind our aiohttp endpoint to our app
## router
app.router.add_static('/static', 'static')
app.router.add_get('/', index)

## We kick off our server
if __name__ == '__main__':
    web.run_app(app)
