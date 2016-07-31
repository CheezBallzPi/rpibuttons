import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
buzzer=18
GPIO.setup(buzzer, GPIO.OUT)

p=GPIO.PWM(buzzer,261)

def play_note(freq, duration):
    p.ChangeFrequency(freq)
    p.start(50)
    time.sleep(duration)
    p.stop() 

C=261

D=294

E=330

song=[(E,.25),(D,.25),(C,.5),(E,.25),(D,.25),(C,.5),(C,0.1),(C,0.1),(C,0.1),(C,0.1),(D,0.1),(D,0.1),(D,0.1),(D,0.1),(E,.25),(D,.25),(C,.25)]

for note in song:
        play_note(note[0]*16,note[1]/2)
        time.sleep(.01)
