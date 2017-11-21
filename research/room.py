# -*- coding: utf-8 -*-
from numpy import *


class Source:
    def __init__(self, position, freq, phase):
        self.position = position
        self.freq = freq
        self.phase = phase
    
    def distTo(self, other):
        return sqrt(sum(square(self.position - other)))
    
    def simulateWaveform(self, observerPos, tStart, tEnd, sampleFreq, mediumVelocity=300, simulateDistance=False):
        t = arange(tStart, tEnd, 1/sampleFreq)
        dist = self.distTo(observerPos);
        factor = 1/dist/dist if simulateDistance else 1.0
        
        return cos(2.0*pi*((t - dist/mediumVelocity)*self.freq - self.phase))

    def getPhaseShiftAt(self, observerPos, mediumVelocity=300, tStart=0):
        return ((self.distTo(observerPos) / mediumVelocity) - tStart) * self.freq + self.phase

class Room:
    def __init__(self, width, height, sources, time=0):
        self.width = width
        self.height = height
        self.sources = sources
        self.time = time
    
    def simulateWaveform(self, observerPos, tStart, tEnd, sampleFreq, mediumVelocity=300, simulateDistance=False):
        return sum(source.simulateWaveform(observerPos, tStart, tEnd, sampleFreq, mediumVelocity, simulateDistance) for source in self.sources)
