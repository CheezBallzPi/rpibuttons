# Raspberry Pi Button Game
# 
# This game makes the seven lights light up in a row very quickly. You must try to 
# press the button when the middle light is lit up. 
# For best use, switch the middle LED with a different color one.
# 
# Written by Jackie Chen
# 
# Why are you still reading this? Look at the actual code!

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

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< Updated upstream
GPIO.output((light1, light2, light3, light4, light5, light6, light7, buzzer), 0)
=======
GPIO.output((light1, light2, light3, light4, light5, light6, light7, light8, buzzer), 0)
>>>>>>> master
GPIO.output(buttonOut, 1)

=======
=======
>>>>>>> 43eb5713a2379e484be7536fffbafe7f5e514703
GPIO.output((light1, light2, light3, light4, light5, light6, light7, light8, buzzer), 0)
GPIO.output(button1Out, 1)
GPIO.output(button2Out, 1)

# buzz() and play() are used for the buzzer. Feel free to copy this if you need to use the buzzer

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

# To edit the tunes, just change the pitch and duration list.
def play(tune):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer, GPIO.OUT)

    x = 0
    if tune == 1:
        # A list of possible pitches? [262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1047]
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

# main
try:
    while True:
      
        # prints 3, 2, 1, GO and lights light up in certain way:
        # 3      O - - - - - O
        # 2      - O - - - O -
        # 1      - - O - O - -
        # GO     - - - O - - -
        print("3")
        GPIO.output((light1, light8), 1)
        buzz(262, 0.5)
        time.sleep(.5)
        print("2")
        GPIO.output((light1, light8), 0)
        GPIO.output((light2, light7), 1)
        buzz(262, 0.5)
        time.sleep(.5)
        print("1")
        GPIO.output((light2, light7), 0)
        GPIO.output((light3, light6), 1)
        buzz(262, 0.5)
        time.sleep(.5)
        print("GO")
        GPIO.output((light3, light6), 0)
        GPIO.output((light4, light5), 1)
        buzz(440, 0.5)
        time.sleep(.5)

        while True:
            GPIO.output((light1, light2, light3, light4, light5, light6, light7, light8, buzzer), 0)

            buttonPressed = False
            
            # Constantly checks if button is pressed, and then moves light. Also checks if you win or not. 
            # This method does not use events, and is the lazy person way of doing it. It is not recommended.
            # But I'm lazy, so derp. :b
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
                if currLight == 9:
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
        GPIO.output((light1, light2, light3, light4, light5, light6, light7, light8, buzzer), 0)
    GPIO.output((light1, light2, light3, light4, light5, light6, light7, light8, buttonOut, buzzer), 0)
except:
    # If it all breaks, turn all pins off.
    GPIO.output((light1, light2, light3, light4, light5, light6, light7, light8, buttonOut, buzzer), 0)
