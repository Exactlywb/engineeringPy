from time import sleep

import matplotlib.pyplot as plt
import numpy as np

import RPi.GPIO as GPIO

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

def buildSin (time, frequency, samplingFrequency):
    x = np.linspace (0, time, time * samplingFrequency)
    y = np.sin (x * 2 * np.pi * frequency)

    plt.plot(x, (y + 1) / 2)
    plt.savefig('sin.png')

    for i in range(time * samplingFrequency):
        num2dac (int((y[i] + 1) / 2 * 255))
        sleep ((float)(1/samplingFrequency))

time                = int (input ("Время работы:"))
frequency           = int (input ("Частота:"))
samplingFrequency   = int (input ("Частота сэмплирования:"))

buildSin (time, frequency, samplingFrequency)

GPIO.output  (diodList, 0)
GPIO.cleanup (diodList)
