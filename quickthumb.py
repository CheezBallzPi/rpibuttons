import RPi.GPIO as GPIO
import time
import player

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
GPIO.setup([button1In, button2In], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([button1Out, button2Out], GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

GPIO.output(lightBuzzList, 0)
GPIO.output(button1Out, 1)
GPIO.output(button2Out, 1)

start = True
time0 = 0

lightList = [2, 3, 4, 17, 27, 22, 10, 9]

def play(song, tempo=72):
    notes = {
        'C': 261.3,
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
    """
    16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87,
    32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74,
    65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5,
    130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.7, 220.0, 233.1, 246.9,
    261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0, 466.2, 493.9,
    523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740.0, 784.0, 830.6, 880.0, 932.3, 987.8,
    1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976,
    2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951,
    4186, 4435, 4699, 4978, 5274, 5588, 5920, 6272, 6645, 7040, 7459, 7902
    """
    oneBeat = 60.0 / tempo
    p = GPIO.PWM(buzzer, 261)
    for (note, duration) in song:
        print("play {}({}) for {} sec".format(note, notes[note], duration))
        realBeat = oneBeat * duration
        play_note(p, notes[note], realBeat)


def play_note(player, freq, beat):
    player.ChangeFrequency(freq)
    player.start(50)
    time.sleep(0.9 * beat)
    player.stop()
    time.sleep(0.1 * beat)
    
def turn_on_n_leds(n):
    GPIO.output(lightList, 0)
    if n < 0:
        n = 1
    on_list = lightList[0:n]
    GPIO.output(on_list, 1)


def map_ms_to_n(ms):
    ranking = [110, 120, 130, 150,
               180, 190, 230, 250]
    n = 1
    for interval in ranking:
        if ms < interval:
            return n
        else:
            n += 1
    return n


def pressed(channel):
    global start
    global time0
    if start:
        time0 = time.time()
        GPIO.output(lightList, 1)
    else:
        GPIO.output(lightList, 0)
        response_time = 1000 * (time.time() - time0)
        print("Your time is {} ms".format(int(response_time)))
        turn_on_n_leds(map_ms_to_n(response_time))
        if response_time < 150:
            player.play(buzzer, [("C", 0.5), ("C", 0.5), ("G", 2)])
        else:
            player.play(buzzer, [("G", 0.5), ("F", 0.5), ("E", 0.5), ("C", 2)])

    start = not start

GPIO.add_event_detect(button1In, GPIO.RISING, callback=pressed, bouncetime=100)

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    # If it all breaks, turn all pins off.
    GPIO.output(lightBuzzButtonList, 0)
