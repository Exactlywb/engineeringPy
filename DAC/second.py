import RPi.GPIO as GPIO
import time

diodList = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode (GPIO.BCM)
GPIO.setup   (diodList, GPIO.OUT)

def decToBinList(decNumber):
    res = [0] * 8
    i = 7
    while i >= 0:
        res[i] = decNumber & 1
        decNumber >>= 1
        i -= 1

    return res

def num2dac(value):
    GPIO.output(diodList, decToBinList(value))   

while True:
    repetitionsNumber = int(input ("Введите число повторений:"))
    if (repetitionsNumber >= 0):
        break
    else:
        print ("Введите число >= 0")
        continue

for i in range (1, repetitionsNumber):
    for diodNum in range(256):
        num2dac (diodNum)
        time.sleep (0.01)
    for diodNum in range (255, -1, -1):
        num2dac (diodNum)  
        time.sleep (0.01)


GPIO.output  (diodList, 0)
GPIO.cleanup (diodList)