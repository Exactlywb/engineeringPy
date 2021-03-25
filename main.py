import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]

def lightEternal (ledNumber):
    realNumber = leds [ledNumber]
    
    GPIO.setmode (GPIO.BCM)
    GPIO.setup   (realNumber, GPIO.OUT)
    GPIO.output  (realNumber, 1)

def lightOff (ledNumber):
    realNumber = leds [ledNumber]

    GPIO.output  (realNumber, 0)
    GPIO.cleanup (realNumber)

def lightUp (ledNumber, period):
    realNumber = leds [ledNumber]
    

    GPIO.setmode (GPIO.BCM)
    GPIO.setup   (realNumber, GPIO.OUT)
    GPIO.output  (realNumber, 1)

    time.sleep   (period)    

    GPIO.output  (realNumber, 0)
    GPIO.cleanup (realNumber)


def blink (ledNumber, blinkCount, blinkPeriod):
    for counter in range (blinkCount):
        lightUp (ledNumber, blinkPeriod)
        time.sleep (blinkPeriod)

def runningLight (count, period):
    for countCircle in range (count):
        for countDiod in range (8):
            lightUp (countDiod, period)

def runningDark (count, period):
    for counter in range(8):
        lightEternal (counter)

    for counter in range(count):
        for counterDiod in range(8):
            lightOff (counterDiod)
            time.sleep (period)
            lightEternal (counterDiod)

    for counter in range(8):
        lightOff (counter)
        
def decToBin (decNumber):
    binConvert     = [0]*8
    countByte      = 7

    while decNumber != 0:
        binConvert [countByte] = decNumber % 2
        countByte -= 1
        decNumber //= 2    

    return binConvert

def lightNumberWithBinPattern (binPattern):
    for diod in range(8):
        if binPattern[7 - diod]:
            lightEternal (diod)
    time.sleep (3)
    for diod in range (8):
        if binPattern [7 - diod]:
            lightOff (diod)    

def lightNumber (number):
    pattern = decToBin (number)
    lightNumberWithBinPattern (pattern)

def move (binPattern, direction):
    if direction:
        elem = binPattern.pop(7)
        binPattern.insert(0, elem)
    else:
        elem = binPattern.pop(0)
        binPattern.insert(7, elem)

    return binPattern

def runningPattern (pattern, direction):
    binPattern = decToBin ( pattern )
    print (binPattern)
    lightNumberWithBinPattern ( binPattern )

    binPattern = move ( binPattern, direction )
    print (binPattern)
    lightNumberWithBinPattern ( binPattern )

def PWM (maxBright, output, step):

    realNumber = leds[output]

    GPIO.setmode (GPIO.BCM)
    GPIO.setup   (realNumber, GPIO.OUT)

    point = GPIO.PWM (realNumber, 50)
    point.start (0)

    for bright in range (0, maxBright, step):
        
        point.ChangeDutyCycle (bright)
        time.sleep (0.5)

    for bright in range (maxBright, 0, -step):
        
        point.ChangeDutyCycle (bright)
        time.sleep (0.5)

    point.stop ()
    GPIO.cleanup ()

runningPattern(128, 0)
#PWM (100, 3, 5)
#lightNumber (24)
#print (decToBin (255))
#runningDark (2, 0.3)
#blink(2,4,1)