# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:26:58 2017

@author: Fons
"""

from numpy import *
from room import *
from matplotlib import pyplot as plt
from matplotlib import patches
from phasemeasurement import *


def probOfPhaseshift(diff):
    #return 1 if abs(diff) < .1 else 0
    return (1 - 2*abs(diff))**3


Fs = 48000

mediumVel = 300

room = Room(1, 1, [
                   Source(array([0, 0]), 200, .1),
                   #Source(array([1, 0]), 300, .1),
                   Source(array([0, 1]), 1300, .1),
                   Source(array([0, 1]), 1700, .1),
                   Source(array([1, 1]), 1000, .1),
                   Source(array([1, 1]), 700, .1)])

room.time = 3.4

observer = array([.3,.4])

tStart = 0.0
tEnd = .05
t = arange(tStart, tEnd, 1/Fs)

plt.ion()


for i,angle in enumerate(linspace(0, 2*pi, 5, endpoint=False)):
    observer[0] = .5 + .25*cos(angle)
    observer[1] = .5 + .25*sin(angle)

    waveform = room.simulateWaveform(observer, tStart, tEnd, Fs, mediumVelocity=mediumVel)
    
    frequencies = [source.freq for source in room.sources]
    phases = getPhaseShifts(waveform, Fs, frequencies)
    
    #plt.plot(t,waveform)
    
    imRes = 64
    imWidth = int(room.width * imRes)
    imHeight = int(room.height * imRes)
    
    image = zeros([imWidth, imHeight])
    
    for ix,x in enumerate(linspace(0, room.width, imRes)):
        for iy,y in enumerate(linspace(0, room.height, imRes)):
            pos = array([x,y])
            prop = 1
            for i, source in enumerate(room.sources):
                diff = phaseDifference(source.getPhaseShiftAt(pos, mediumVelocity=mediumVel, tStart=tStart), phases[i])
                prop *= probOfPhaseshift(diff)
            image[ix,iy] = prop
    
    foundpos = unravel_index(argmax(image),image.shape)
    print(foundpos)
    
    
    
    intobserver = (int(observer[0]*imRes),int(observer[1]*imRes))
    '''
    for ix in range(imWidth):
        image[ix,intobserver[1]] = 1 - image[ix,intobserver[1]]
    for iy in range(imHeight):
        image[intobserver[0], iy] = 1 - image[intobserver[0], iy]
    
    for ix in range(imWidth):
        image[ix,foundpos[1]] = 1
    for iy in range(imHeight):
        image[foundpos[0], iy] = 1
    '''
    fig,ax = plt.subplots(1)
    ax.imshow(transpose(image))