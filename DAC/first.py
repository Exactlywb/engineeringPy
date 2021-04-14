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
    value = int(input ("Введите число (-1 для выхода):"))
    if value == -1:
        break
    else:
        num2dac (value)
        

GPIO.output  (diodList, 0)
GPIO.cleanup (diodList)