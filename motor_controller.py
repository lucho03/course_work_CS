import RPi.GPIO as GPIO

GPIO.setwarnings(False)

front_left_front_power_a = 21 # orange
front_left_input_1 = 16 # yellow
front_left_input_2 = 20 # red

front_right_front_power_b = 26 # white
front_right_input_3 = 19 # green
front_right_input_4 = 13 # blue

back_left_back_power_a = 4 # brown
back_left_input_1 = 17 # green
back_left_input_2 = 27 # dark blue

back_right_back_power_b = 24 # white
back_right_input_3 = 23 # violet
back_right_input_4 = 22 # grey

GPIO.setmode(GPIO.BCM)

GPIO.setup(front_left_input_1, GPIO.OUT)
GPIO.setup(front_left_input_2, GPIO.OUT)
GPIO.setup(front_left_front_power_a, GPIO.OUT)

GPIO.setup(front_right_input_3, GPIO.OUT)
GPIO.setup(front_right_input_4, GPIO.OUT)
GPIO.setup(front_right_front_power_b, GPIO.OUT)

GPIO.setup(back_left_input_1, GPIO.OUT)
GPIO.setup(back_left_input_2, GPIO.OUT)
GPIO.setup(back_left_back_power_a, GPIO.OUT)

GPIO.setup(back_right_input_3, GPIO.OUT)
GPIO.setup(back_right_input_4, GPIO.OUT)
GPIO.setup(back_right_back_power_b, GPIO.OUT)

front_power_a = GPIO.PWM(front_left_front_power_a, 100)
front_power_b = GPIO.PWM(front_right_front_power_b, 100)
front_power_a.start(50)
front_power_b.start(50)

power_a = GPIO.PWM(back_left_back_power_a, 100)
power_b = GPIO.PWM(back_right_back_power_b, 100)
power_a.start(50)
power_b.start(50)

GPIO.output(front_left_input_1, GPIO.LOW)
GPIO.output(front_left_input_2, GPIO.LOW)

GPIO.output(front_right_input_3, GPIO.LOW)
GPIO.output(front_right_input_4, GPIO.LOW)

GPIO.output(back_left_input_1, GPIO.LOW)
GPIO.output(back_left_input_2, GPIO.LOW)

GPIO.output(back_right_input_3, GPIO.LOW)
GPIO.output(back_right_input_4, GPIO.LOW)

def move(direction, speed):
    if direction == 'forward':
        front_power_a.start(speed)
        front_power_b.start(speed)
        power_a.start(speed)
        power_b.start(speed)
        
        GPIO.output(front_left_input_1, GPIO.HIGH)
        GPIO.output(front_left_input_2, GPIO.LOW)
        
        GPIO.output(front_right_input_3, GPIO.HIGH)
        GPIO.output(front_right_input_4, GPIO.LOW)
            
        GPIO.output(back_left_input_1, GPIO.HIGH)
        GPIO.output(back_left_input_2, GPIO.LOW)
        
        GPIO.output(back_right_input_3, GPIO.HIGH)
        GPIO.output(back_right_input_4, GPIO.LOW)
    elif direction == 'backward':
        front_power_a.start(speed)
        front_power_b.start(speed)
        power_a.start(speed)
        power_b.start(speed)
        
        GPIO.output(front_left_input_1, GPIO.LOW)
        GPIO.output(front_left_input_2, GPIO.HIGH)
        
        GPIO.output(front_right_input_3, GPIO.LOW)
        GPIO.output(front_right_input_4, GPIO.HIGH)
        
        GPIO.output(back_left_input_1, GPIO.LOW)
        GPIO.output(back_left_input_2, GPIO.HIGH)
        
        GPIO.output(back_right_input_3, GPIO.LOW)
        GPIO.output(back_right_input_4, GPIO.HIGH)
    elif direction == 'right':
        front_power_a.start(speed)
        front_power_b.start(speed)
        power_a.start(speed)
        power_b.start(speed)
        
        GPIO.output(front_left_input_1, GPIO.HIGH)
        GPIO.output(front_left_input_2, GPIO.LOW)
        
        GPIO.output(front_right_input_3, GPIO.LOW)
        GPIO.output(front_right_input_4, GPIO.HIGH)
        
        GPIO.output(back_left_input_1, GPIO.LOW)
        GPIO.output(back_left_input_2, GPIO.HIGH)
        
        GPIO.output(back_right_input_3, GPIO.HIGH)
        GPIO.output(back_right_input_4, GPIO.LOW)
    elif direction == 'left':
        front_power_a.start(speed)
        front_power_b.start(speed)
        power_a.start(speed)
        power_b.start(speed)
        
        GPIO.output(front_left_input_1, GPIO.LOW)
        GPIO.output(front_left_input_2, GPIO.HIGH)
        
        GPIO.output(front_right_input_3, GPIO.HIGH)
        GPIO.output(front_right_input_4, GPIO.LOW)
        
        GPIO.output(back_left_input_1, GPIO.HIGH)
        GPIO.output(back_left_input_2, GPIO.LOW)
        
        GPIO.output(back_right_input_3, GPIO.LOW)
        GPIO.output(back_right_input_4, GPIO.HIGH)
    elif direction == 'stop':
        GPIO.output(front_left_input_1, GPIO.LOW)
        GPIO.output(front_left_input_2, GPIO.LOW)
        
        GPIO.output(front_right_input_3, GPIO.LOW)
        GPIO.output(front_right_input_4, GPIO.LOW)
        
        GPIO.output(back_left_input_1, GPIO.LOW)
        GPIO.output(back_left_input_2, GPIO.LOW)
        
        GPIO.output(back_right_input_3, GPIO.LOW)
        GPIO.output(back_right_input_4, GPIO.LOW)
    elif direction == 'exit':
        GPIO.cleanup()
