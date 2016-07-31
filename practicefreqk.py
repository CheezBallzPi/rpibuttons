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


def button1Pressed(channel1):
    song_A= [('C', 0.5), ('C', 0.5), ('G', 0.5), ('G', 0.5),
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
    
    song_B=[('C', 0.5), ('C', 0.5), ('D', 0.5), ('E', 0.5), ('C', 0.5), ('E', 0.5), ('D', 0.5),
            ('C', 0.5), ('C', 0.5), ('D', 0.5), ('E', 0.5), ('C',1), ('B2',1)]

    allSongs=[song_A,song_B]
    
    print("button pressed", selectedSong)
    GPIO.output(lightList[0], 1)
    player.play(buzzer, allSongs[selectedSong], tempo=120)

GPIO.add_event_detect(button1In,
                      GPIO.RISING,
                      callback=button1Pressed,
                      bouncetime=100)

selectedSong = 0
def button2Pressed(channel2):
    global selectedSong
    selectedSong = selectedSong+1
    if selectedSong > 1:
        selectedSong = 0
    print("select song {}".format(selectedSong))

GPIO.add_event_detect(button2In,
                      GPIO.RISING,
                      callback=button2Pressed,
                      bouncetime=1000)
try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.output(lightBuzzButtonList, 0)
