import time

# Import the MCP4725 module.
import Adafruit_MCP4725

# Import the ADS1x15 module.
import Adafruit_ADS1x15 as ADS

# help test sine waves 
import numpy as np

# Create a DAC instance.
dac = Adafruit_MCP4725.MCP4725()

# Create an ADS1115 ADC (16-bit) instance.
adc0 = ADS.ADS1115(address=0x49, busnum=1)
adc0._data_rate_config(860)

GAIN = 1

# Start continuous ADC conversions on channel 0 using the previously set gain
# value.  Note you can also pass an optional data_rate parameter, see the simpletest.py
# example and read_adc function for more infromation.
try: adc0.start_adc(0, gain=GAIN)
except Exception as e: print(e)

Fs = 300*10
f = 300
sample = 300*10
x = np.arange(sample)
y = np.sin(np.pi * f * x / Fs)


print('Press Ctrl-C to quit...')
i = 0
while True:
    #print('Setting voltage to 0!')
    
    try: dac.set_voltage(  int( (adc0.get_last_result() + 400) /800*4069 ) )
    except Exception as e: print(e)
    
    #print(int( (adc0.get_last_result() + 400) /800*4069 ))
    #dac.set_voltage(  (int(y[i])+1) *4096 )
    #i+=1
    
    
    
    
    #time.sleep(3.0)
    #print('Setting voltage to 1/2 Vdd!')
    #dac.set_voltage(2048)  # 2048 = half of 4096
    
