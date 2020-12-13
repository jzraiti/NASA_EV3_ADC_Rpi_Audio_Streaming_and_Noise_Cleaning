# Project 1: ADC Gstreamer
Begin by installing libraries for ADC and DAC

Then install Gstreamer, can do this 

## ADC and DAC

## Jasons ADC to Gstreamer

## Jasons WAV to Gstreamer

## NASA_EV3_Audio_Streaming-master

## gstreamer_client

You can find the libraries for the ADC at
https://github.com/adafruit/Adafruit_Python_ADS1x15

You can find the libraries for the DAC at 
https://github.com/adafruit/Adafruit_Python_MCP4725



useful things to know about gstreamer:

Test installation of Gstreamer and configuration of Gstreamer on Rpi with:
	gst-launch-1.0 audiotestsrc ! audioconvert ! audioresample ! alsasink
You should hear a constant tone sine wave. 
If you do not hear anything, try replacing alsasink with autoaudiosink. 
This method will attempt to automatically recognize the sound card for your device. 
If you want to try testing a Raspberrypi microphone use alsasrc.

if you edit C file then compile with:
gcc -Wall <cfile> -o <compiledfile> -lpthread $(pkg-config --cflags --libs gstreamer-1.0)
