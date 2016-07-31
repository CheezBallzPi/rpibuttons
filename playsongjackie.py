# import GPIO and time
import RPi.GPIO as GPIO
import time
import player

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
currLight = 0
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

GPIO.output(lightList[0], 1)

def songChooseButton(channel):
    global currLight
    GPIO.output(lightList[currLight], 0)
    if currLight == 7:
        currLight = 0
    else:
        currLight += 1
    GPIO.output(lightList[currLight], 1)

def buttonPressed(channel):
    song1 = [('C', 0.5), ('C', 0.5), ('G', 0.5), ('G', 0.5),
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

    song2 = [('E', 0.5), ('lB', 0.5), ('C', 1),
             ('E', 0.5), ('lB', 0.5), ('C', 1),
             ('C', 0.25), ('C', 0.25), ('C', 0.25), ('C', 0.25),
             ('D', 0.25), ('D', 0.25), ('D', 0.25), ('D', 0.25),
             ('E', 0.5), ('lB', 0.5), ('C', 2)]

    song3 = [('E', 1),('E', 1),('F', 1),('G', 1),('G', 1),('F', 1),('E', 1),('D', 1),
             ('C', 1),('C', 1),('D', 1),('E', 1),('E', 1.25),('D', 0.25),('D', 1),
             ('E', 1),('E', 1),('F', 1),('G', 1),('G', 1),('F', 1),('E', 1),('D', 1),
             ('C', 1),('C', 1),('D', 1),('E', 1),('E', 1.25),('C', 0.25),('C', 1)]
    song4 = [('G', 1),('E', 1),('G', 1.5),('E', 1),('C', 1.5),('D', 1),('E', 1),('F', 1.25),('D', 1.25),('G', 1.25),('C', 1),('B', 2)]
    song5 = []
    song6 = []
    song7 = []
    song8 = []
    songList = [song1, song2, song3, song4, song5, song6, song7, song8]
    print("button pressed")
    GPIO.output(lightList[0], 1)
    player.play(buzzer, songList[currLight], tempo=120)

GPIO.add_event_detect(button1In,
                      GPIO.RISING,
                      callback=buttonPressed,
                      bouncetime=1000)

GPIO.add_event_detect(button2In,
                      GPIO.RISING,
                      callback=songChooseButton,
                      bouncetime=1000)
try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.output(lightBuzzButtonList, 0)
