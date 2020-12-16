# Project 1: ADC Gstreamer



## ADC and DAC
Begin by installing libraries for ADC and DAC

You can find the libraries for the ADC at
https://github.com/adafruit/Adafruit_Python_ADS1x15

You can find the libraries for the DAC at 
https://github.com/adafruit/Adafruit_Python_MCP4725

## Jasons ADC to Gstreamer

Install Gstreamer... this step can be done via ronnies code which will also build a compiled c file. 

## Jasons WAV to Gstreamer

Install Gstreamer... this step can be done via ronnies code which will also build a compiled c file. 

## NASA_EV3_Audio_Streaming-master

Ronnies original project. Here for ease of access and because it would be good to familiarize with for this project.

## gstreamer_client

Here are edited versions of Ronnies gstreamer pipeline (G_CLIENT). Should have same dependencies.

useful things to know about gstreamer:

Test installation of Gstreamer and configuration of Gstreamer on Rpi with:
	gst-launch-1.0 audiotestsrc ! audioconvert ! audioresample ! alsasink
You should hear a constant tone sine wave. 
If you do not hear anything, try replacing alsasink with autoaudiosink. 
This method will attempt to automatically recognize the sound card for your device. 
If you want to try testing a Raspberrypi microphone use alsasrc.

if you edit C file then compile with:
gcc -Wall <cfile> -o <compiledfile> -lpthread $(pkg-config --cflags --libs gstreamer-1.0)
	



