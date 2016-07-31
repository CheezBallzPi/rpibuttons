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
