# Simple demo of continuous ADC conversion mode for channel 0 of the ADS1x15 ADC.
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15 as ADS



# Create an ADS1115 ADC (16-bit) instance.
# address is adjusted by grounding address pin !!!
adc0 = ADS.ADS1115(address=0x49, busnum=1)
adc0._data_rate_config(860)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 16

# Note you can also call start_adc_difference() to take continuous differential
# readings.  See the read_adc_difference() function in differential.py for more
# information and parameter description.

# Start continuous ADC conversions on channel 0 using the previously set gain
# value.  Note you can also pass an optional data_rate parameter, see the simpletest.py
# example and read_adc function for more infromation.
try: adc0.start_adc_difference(1, gain=GAIN, data_rate = 860)
except Exception as e: print(e)

#try: adc1.start_adc(3, gain=GAIN)
#except Exception as e: print(e)
# Once continuous ADC conversions are started you can call get_last_result() to
# retrieve the latest result, or stop_adc() to stop conversions.

# Read channel 0 for 5 seconds and print out its values.
print('Reading ADS1x15 channel 0 for 1 seconds...')
start = time.time()
value = 0 

raw_data = []

while (time.time() - start) <= 60.0:
    # Read the last ADC conversion value and print it out.
    try: value0 = adc0.read_adc_difference(1, gain=GAIN, data_rate = 860)
    except Exception as e: print(e)
    
    # WARNING! If you try to read any other ADC channel during this continuous
    # conversion (like by calling read_adc again) it will disable the
    # continuous conversion!
    
    print('Channel 0: {0}'.format(value0), hex(value0))
    

    #raw_data.append(value0)
    # Sleep for half a second.
    time.sleep(.5)

# Stop continuous conversion.  After this point you can't get data from get_last_result!
adc0.stop_adc()
#adc1.stop_adc()
print(raw_data)
#############################
f = open("testfile860SineWaveDifferential2.txt","a")
for line in raw_data:
    f.write(str(line))
    f.write("\n")
f.close()


