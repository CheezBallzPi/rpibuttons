import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sleepTime = 0.03


light1 = 2
light2 = 3
light3 = 4
light4 = 14
light5 = 15
light6 = 17
light7 = 27

currLight = 2

lightList = [light1,
             light2,
             light3,
             light4,
             light5,
             light6,
             light7]

buttonIn = 22
buttonOut = 23

# PWM pin is pin 18

buzzer = 18

GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)
GPIO.setup(light3, GPIO.OUT)
GPIO.setup(light4, GPIO.OUT)
GPIO.setup(light5, GPIO.OUT)
GPIO.setup(light6, GPIO.OUT)
GPIO.setup(light7, GPIO.OUT)

GPIO.setup(buttonIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonOut, GPIO.OUT)

GPIO.setup(buzzer, GPIO.OUT)

GPIO.output((light1, buzzer), 0)
GPIO.output(buttonOut, 1)


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
