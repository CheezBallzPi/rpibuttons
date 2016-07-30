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

def play(song, tempo=72):
    notes = {
        'C': 261,
        'C#': 277,
        'D': 294,
        'Eb': 311,
        'E': 330,
        'F': 349,
        'F#': 370,
        'G': 392,
        'G#': 415,
        'A': 440,
        'Bb': 466,
        'B': 494
    }
    oneBeat = 60.0 / tempo
    p = GPIO.PWM(buzzer, 261)
    for (note, duration) in song:
        print("play {}({}) for {} sec".format(note, notes[note], duration))
        p.ChangeFrequency(notes[note])
        realBeat = oneBeat * duration
        play_note(p, note, realBeat)


def play_note(player, freq, beat):
    player.ChangeFrequency(freq)
    player.start(50)
    time.sleep(0.9 * beat)
    player.stop()
    time.sleep(0.1 * beat)

#    p.stop()


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
    GPIO.output(light1, 1)
    play(song, tempo=120)

GPIO.add_event_detect(buttonIn,
                      GPIO.RISING,
                      callback=buttonPressed,
                      bouncetime=100)
try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.output((light1,
                 light2,
                 light3,
                 light4,
                 light5,
                 light6,
                 light7,
                 buttonOut,
                 buzzer), 0)
