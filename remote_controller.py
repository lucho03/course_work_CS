import RPi.GPIO as GPIO

from flask import Flask, render_template
from flask_socketio import SocketIO

from motor_controller import move

from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from time import sleep

from threading import Thread, Lock

app = Flask(__name__)
socketio = SocketIO(app)
sensor = GroveUltrasonicRanger(5)

@app.route("/")
def controller():
    return render_template('controller.html')

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('controller')
def handle_event(message):
    print('direction: ' + message['direction'] + ', speed: ' + str(message['speed']))
    data.update( message['direction'] )
    move(message['direction'], message['speed'])

def handle_sensor(data):
    while True:
        distance = int(sensor.get_distance())
        if distance < 20 and data.get() == 'forward':
            move('stop', 0)
        #print(f"Distance: {distance} cm")
        #print(data.get())
        sleep(0.1)

class Data:
	def __init__(self):
		self.direction = 'stop'
		self.lock = Lock()
	def update(self, new_direction):
		with self.lock:
			self.direction = new_direction
	def get(self):
		with self.lock:
			return self.direction

if __name__ == '__main__':
    data = Data()
    t1 = Thread(target=handle_sensor, args=(data,), daemon=True)
    t1.start()
    socketio.run(app, host='0.0.0.0')
    #app.run(host="0.0.0.0")
    #flask --app remote_controller run --host=0.0.0.0

