# Simple demo of continuous ADC conversion mode for channel 0 of the ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15 as ADS

#struct may allow me to convert my data to signed 16bit little-endian
import struct


# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = ADS.ADS1115(address=0x49, busnum=1)
#adc._data_rate_config(860)

adc0 = ADS.ADS1115(address=0x49, busnum=1)
adc0._data_rate_config(860)


#adc1 = ADS.ADS1115(address=0x49, busnum=1)
#adc1._data_rate_config(860)

#adc = ADS.ADS1115(i2c, gain=1, data_rate=860)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Start continuous ADC conversions on channel 0 using the previously set gain
# value.  Note you can also pass an optional data_rate parameter, see the simpletest.py
# example and read_adc function for more infromation.
try: adc0.start_adc(0, gain=GAIN)
except Exception as e: print(e)

#try: adc3.start_adc(3, gain=GAIN)
#except Exception as e: print(e)
# Once continuous ADC conversions are started you can call get_last_result() to
# retrieve the latest result, or stop_adc() to stop conversions.

# Note you can also call start_adc_difference() to take continuous differential
# readings.  See the read_adc_difference() function in differential.py for more
# information and parameter description.

# Read channel 0 for 5 seconds and print out its values.
print('Reading ADS1x15 channel 0 for 120 seconds...')
start = time.time()
value = 0 

#raw_data = []

f = open("300hzSineTone.raw","a")
#for line in raw_data:
    #f.write(str(line))
    #f.write("\n")
    
while (time.time() - start) <= 120.0:
    # Read the last ADC conversion value and print it out.
    try: value0 = adc0.get_last_result()
    except Exception as e: print(e)
    
    #try: value1 = adc1.get_last_result()
    #except Exception as e: print(e)
    # WARNING! If you try to read any other ADC channel during this continuous
    # conversion (like by calling read_adc again) it will disable the
    # continuous conversion!
    # print('Channel 0: {0}'.format(value), hex(value))
    #TrueValue = adc.read_adc_difference(0, gain=GAIN)
    #print('Channel 0 : {0}'.format(value0), hex(value0))
    
    
    f.write(str(struct.pack('<h',value0)))
    f.write("\n")
    
    #1
    #f.write(str(value0))
    #f.write("\n")
    #2
    #f.write(str(value0))
    #f.write("\n")
    #3
    #f.write(str(value0))
    #f.write("\n")
    #4
    #f.write(str(value0))
    #f.write("\n")
    #5
    #f.write(str(value0))
    #f.write("\n")
    #6
    #f.write(str(value0))
    #f.write("\n")
    #7
    #f.write(str(value0))
    #f.write("\n")
    #8
    #f.write(str(value0))
    #f.write("\n")
    #9
    #f.write(str(value0))
    #f.write("\n")
    
    #raw_data.append(value0)
    
    
    # Sleep for half a second.
    #time.sleep()

# Stop continuous conversion.  After this point you can't get data from get_last_result!
adc0.stop_adc()
#adc1.stop_adc()

f.close()


