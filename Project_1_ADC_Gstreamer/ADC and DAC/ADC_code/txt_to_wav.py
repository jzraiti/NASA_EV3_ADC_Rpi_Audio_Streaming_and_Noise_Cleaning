# Simple demo of continuous ADC conversion mode for channel 0 of the ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15 as ADS

import wave
 
import struct
 

###############################################
#Write a wav file from our raw data

raw_data = []
with open('300hzSineTone.txt','r') as file:
    for line in file:
        cleanLine = line[:-1]
        raw_data.append(int(cleanLine))
        
print(len(raw_data))
print(max(raw_data))
num_samples = len(raw_data) #total number of samples taken!!!
sampling_rate = 860.0 #how many samples per second !!!! 
amplitude = 1
 
file2 = "300hzSineTone.wav"
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2 #2 bytes per sample or 16 bit
wav_file=wave.open(file2, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in raw_data:
    #print(s)
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))

