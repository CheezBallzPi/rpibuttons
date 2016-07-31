# import GPIO and time
import RPi.GPIO as GPIO
import time


# Set GPIO mode to Broadcom
GPIO.setmode(GPIO.BCM)

button1In = 23
button1Out = 24
button2In = 8
button2Out = 7
# PWM pin is pin 18
buzzer = 18

# lightList will be used in a for loop later
lightList = [2, 3, 4, 17, 27, 22, 10, 9]
lightBuzzList = lightList + [buzzer]
lightBuzzButtonList = lightBuzzList + [button1Out, button2Out]

# Setting up all pins

GPIO.setup(lightList, GPIO.OUT)

GPIO.setup(button1In, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button1Out, GPIO.OUT)
GPIO.setup(button2In, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2Out, GPIO.OUT)

GPIO.setup(buzzer, GPIO.OUT)


GPIO.output(lightBuzzList, 0)


GPIO.output(button1Out, 1)
GPIO.output(button2Out, 1)


def buttonPressed(channel):
    song = [('C', 0.5), ('C', 0.5), ('G', 0.5), ('G', 0.5),
            ('A', 0.5), ('A', 0.5), ('G', 1),
            ('F', 0.5), ('F', 0.5), ('E', 0.5), ('E', 0.5),
            ('D', 0.5), ('D', 0.5), ('C', 1),
            ('G', 0.5), ('G', 0.5), ('F', 0.5), ('F', 0.5),
            ('E', 0.5), ('E', 0.5), ('D', 1),
            ('G', 0.5), ('G', 0.5), ('F', 0.5), ('F', 0.5),
            ('E', 0.5), ('E', 0.5), ('D', 1),
            ('C', 0.5), ('C', 0.5), ('G', 0.5), ('G', 0.5),
            ('A', 0.5), ('A', 0.5), ('G', 1),
            ('F', 0.5), ('F', 0.5), ('E', 0.5), ('E', 0.5),
            ('D', 0.5), ('D', 0.5), ('C', 1)]
    print("button pressed")
    GPIO.output(lightList[0], 1)
    player.play(buzzer, song, tempo=120)

GPIO.add_event_detect(button1In,
                      GPIO.RISING,
                      callback=buttonPressed,
                      bouncetime=100)
try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.output(lightBuzzButtonList, 0)
