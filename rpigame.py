import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sleepTime = 0.05

buttonPressed = False

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

GPIO.output((light1, light2, light3, light4, light5, light6, light7, buzzer), 0)
GPIO.output(buttonOut, 1)


def buzz(pitch, duration):  # create the function “buzz” and feed it the pitch and duration)
    if pitch == 0:
        time.sleep(duration)
        return
    period = 1.0 / pitch  # in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
    delay = period / 2  # calcuate the time for half of the wave
    cycles = int(duration * pitch)  # the number of waves to produce is the duration times the frequency

    for i in range(cycles):  # start a loop from 0 to the variable “cycles” calculated above
        GPIO.output(buzzer, True)  # set pin 18 to high
        time.sleep(delay)  # wait with pin 18 high
        GPIO.output(buzzer, False)  # set pin 18 to low
        time.sleep(delay)  # wait with pin 18 low


def play(tune):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer, GPIO.OUT)

    x = 0
    print("Playing tune ", tune)
    if tune == 1:
        # pitches = [262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1047]
        # duration = 0.1
        pitches = [392, 349, 330]
        duration = [0.4, 0.4, 2]
        for p in pitches:
            buzz(p, duration[x])  # feed the pitch and duration to the function, “buzz”
            time.sleep(duration[x] * 0.5)
            x += 1
    elif tune == 2:
        # pitches = [262, 330, 392, 523, 1047]
        pitches = [262, 262, 262, 349]
        # duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0, 5]
        duration = [0.2, 0.2, 0.2, 1]
        for p in pitches:
            buzz(p, duration[x])  # feed the pitch and duration to the function, “buzz”
            time.sleep(duration[x] * 0.5)
            x += 1

try:
    while True:
        print("3")
        GPIO.output((light1, light7), 1)
        buzz(262, 0.5)
        time.sleep(.5)
        print("2")
        GPIO.output((light1, light7), 0)
        GPIO.output((light2, light6), 1)
        buzz(262, 0.5)
        time.sleep(.5)
        print("1")
        GPIO.output((light2, light6), 0)
        GPIO.output((light3, light5), 1)
        buzz(262, 0.5)
        time.sleep(.5)
        print("GO")
        GPIO.output((light3, light5), 0)
        GPIO.output(light4, 1)
        buzz(440, 0.5)
        time.sleep(.5)

        while True:
            GPIO.output((light1, light2, light3, light4, light5, light6, light7, buzzer), 0)

            buttonPressed = False

            for light in lightList:
                GPIO.output(light, 1)
                currLight = light
                if GPIO.input(buttonIn):
                    buttonPressed = True
                    break
                time.sleep(sleepTime)
                if GPIO.input(buttonIn):
                    buttonPressed = True
                    break
                time.sleep(sleepTime)
                GPIO.output(light, 0)
            if buttonPressed:
                print("Button Pressed!")
                print(currLight)
                if currLight == 14:
                    print("You Win!")
                    play(2)
                else:
                    print("You Lose...")
                    play(1)
                print("Press Button to play again.")
                print(GPIO.input(buttonIn))
                while GPIO.input(buttonIn) is 0:
                    continue
                break
        GPIO.output((light1, light2, light3, light4, light5, light6, light7, buzzer), 0)
    GPIO.output((light1, light2, light3, light4, light5, light6, light7, buttonOut, buzzer), 0)
except KeyboardInterrupt:
    GPIO.output((light1, light2, light3, light4, light5, light6, light7, buttonOut, buzzer), 0)
