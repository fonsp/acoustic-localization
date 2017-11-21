import numpy as np
from matplotlib import pyplot as plt
from collections import namedtuple


def getPhaseShifts(waveform, sampleFreq, frequencies):
    num = np.size(waveform)
    y = np.fft.fft(waveform)
    phase = -np.angle(y)[0:num//2]/2/np.pi
    getIndex = lambda freq: int(freq/(sampleFreq/2)*num/2)
    return [phase[getIndex(f)] for f in frequencies]


def phaseDifference(phaseA, phaseB):
    phaseA = phaseA % 1
    phaseB = phaseB % 1
    diff = phaseA - phaseB
    if diff > .5:
        return 1 - diff
    if diff < -.5:
        return 1 + diff
    return diff

'''
Waveprops = namedtuple('Waveprops', ['freq','phase'])

num = 1001
Fs = num/1;

waves = [Waveprops(50,.9), Waveprops(70,0.4)]

t, dt = np.linspace(0, 1, num, endpoint=False, retstep=True)
x = sum(np.cos(2*np.pi*(t*wave.freq-wave.phase)) for wave in waves)
x += np.random.randn(np.size(x))

Fs = 1/dt

y = np.fft.fft(x)

f = np.linspace(0,Fs/2, num//2, endpoint=False)
amplitude = np.abs(y)[0:num//2]
phase = -np.angle(y)[0:num//2]/2/np.pi

plt.plot(f,amplitude)
plt.plot(f,phase)
#plt.xlim([0,.1])
plt.show()

getIndex = lambda freq: int(freq/(Fs/2)*num/2)

print(amplitude[getIndex(50)])
print(amplitude[getIndex(70)])
print(getPhaseShifts(x, Fs, [50, 70]))
'''