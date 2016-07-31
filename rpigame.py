# Raspberry Pi Button Game
#
# This game makes the seven lights light up in a row
# very quickly. You must try to
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

currLight = 2


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


# buzz() and play() are used for the buzzer.
# Feel free to copy this if you need to use the buzzer
def buzz(pitch, duration):
    """
    create the function “buzz” and feed it the pitch and duration)
    @params: pitch
    """
    if pitch == 0:
        time.sleep(duration)
        return
    period = 1.0 / pitch
    # in physics, the period (sec/cyc) is
    # the inverse of the frequency (cyc/sec)
    delay = period / 2
    # calcuate the time for half of the wave
    cycles = int(duration * pitch)
    # the number of waves to produce is the duration times the frequency

    for i in range(cycles):
        # start a loop from 0 to
        # the variable “cycles” calculated above
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
        # A list of possible pitches?
        # [262, 294, 330, 349, 392,
        #  440, 494, 523, 587, 659,
        #  698, 784, 880, 988, 1047]
        pitches = [392, 349, 330]
        duration = [0.4, 0.4, 2]
        for p in pitches:
            buzz(p, duration[x])
            # feed the pitch and duration to the function, “buzz”
            time.sleep(duration[x] * 0.5)
            x += 1
    elif tune == 2:
        # pitches = [262, 330, 392, 523, 1047]
        pitches = [262, 262, 262, 349]
        # duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0, 5]
        duration = [0.2, 0.2, 0.2, 1]
        for p in pitches:
            buzz(p, duration[x])
            # feed the pitch and duration to the function, “buzz”
            time.sleep(duration[x] * 0.5)
            x += 1

# main
try:
    while True:
        # prints 3, 2, 1, GO and lights light up in certain way:
        # 3      O - - - - - - O
        # 2      - O - - - - O -
        # 1      - - O - - O - -
        # GO     - - - O O - - -
        number_lights_2 = len(lightList) // 2
        for step in range(0, number_lights_2):
            if step == number_lights_2 - 1:
                print("GO")
            else:
                print(number_lights_2 - 1 - step)
            if step > 0:
                GPIO.output((lightList[step - 1],
                             lightList[number_lights_2 * 2 - step]), 0)
            GPIO.output((lightList[step],
                         lightList[number_lights_2 * 2 - 1 - step]), 1)
            if step == number_lights_2 - 1:
                buzz(440, 0.5)
            else:
                buzz(262, 0.5)
            time.sleep(.5)

        while True:
            GPIO.output(lightBuzzList, 0)

            buttonPressed = False

            # Constantly checks if button is pressed,
            # and then moves light. Also checks if you win or not.
            # This method does not use events, and is the lazy
            # person way of doing it. It is not recommended.
            # But I'm lazy, so derp. :b
            for light in lightList:
                GPIO.output(light, 1)
                currLight = light
                if GPIO.input(button1In):
                    buttonPressed = True
                    break
                time.sleep(sleepTime)
                if GPIO.input(button1In):
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
                print(GPIO.input(button1In))
                while GPIO.input(button1In) is 0:
                    continue
                break

        GPIO.output(lightBuzzList, 0)
    GPIO.output(lightBuzzButtonList, 0)

except KeyboardInterrupt:
    # If it all breaks, turn all pins off.
    GPIO.output(lightBuzzButtonList, 0)
