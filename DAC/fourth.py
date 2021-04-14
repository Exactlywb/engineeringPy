from time import sleep

import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

import RPi.GPIO as GPIO

diodNum = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode (GPIO.BCM)
GPIO.setup   (diodNum, GPIO.OUT, initial=GPIO.LOW)

def decToBinList(decNumber):
    res = [0] * 8
    i = 7
    while i >= 0:
        res[i] = decNumber & 1
        decNumber >>= 1
        i -= 1

    return res

def num2dac(value):
    GPIO.output(diodNum, decToBinList(value))   

def wav(fname):
    sampleRate, data = wavfile.read(fname)
    print(f"число каналов: {data.shape[1]}")

    length = data.shape[0] / sampleRate
    print(f"длительность аудиозаписи: {length}")
    print(f"частота семплирования: {sampleRate}")

    amplitude = max(data[:, 0].max(), data[:, 0].min())
    print(f"амплитуда: ", amplitude)
    normalizedData = (data[:, 0] / amplitude + 1) / 2

    plt.plot(np.linspace(0, length, data.shape[0]), normalizedData, linewidth = 0.5)
    plt.savefig('wav.png')

    for i in data[:, 0]:
        num2dac (int((int(i) + 32514) / 256))

wav ('SOUND.WAV')

GPIO.output(diodNum, GPIO.LOW)
GPIO.cleanup()

GPIO.output(diodNum, GPIO.LOW)
GPIO.cleanup()
