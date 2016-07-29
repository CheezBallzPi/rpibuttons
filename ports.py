# import GPIO and time
import RPi.GPIO as GPIO
import time

# Set GPIO mode to Broadcom
GPIO.setmode(GPIO.BCM)

# Setting some constants
sleepTime = 0.05
buttonPressed = False

# Setting LED Ports and other ports
light1 = 2
light2 = 3
light3 = 4
light4 = 17
light5 = 27
light6 = 22
light7 = 10
light8 = 9

currLight = 2

# lightList will be used in a for loop later
lightList = [light1,
             light2,
             light3,
             light4,
             light5,
             light6,
             light7,
             light8]

button1In = 23
button1Out = 24
button2In = 8
button2Out = 7
# PWM pin is pin 18
buzzer = 18

# Setting up all pins
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)
GPIO.setup(light3, GPIO.OUT)
GPIO.setup(light4, GPIO.OUT)
GPIO.setup(light5, GPIO.OUT)
GPIO.setup(light6, GPIO.OUT)
GPIO.setup(light7, GPIO.OUT)
GPIO.setup(light8, GPIO.OUT)

GPIO.setup(button1In, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button1Out, GPIO.OUT)
GPIO.setup(button2In, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2Out, GPIO.OUT)

GPIO.setup(buzzer, GPIO.OUT)

GPIO.output((light1, light2, light3, light4, light5, light6, light7, light8, buzzer), 0)
GPIO.output(button1Out, 1)
GPIO.output(button2Out, 1)
