## ADC to DAC 
Connects microphone input using ADC to speaker output using DAC

You will need to have ADC and DAC library dependencies:

You can find the libraries for the ADC at
https://github.com/adafruit/Adafruit_Python_ADS1x15

You can find the libraries for the DAC at 
https://github.com/adafruit/Adafruit_Python_MCP4725

## ADC code
Here are edited files for testing different methods of calling the ADC (ADS1115)

## ALTERNATE HARDWARES:

Maxim adc and dev board: $157.50

https://www.maximintegrated.com/en/products/analog/data-converters/analog-to-digital-converters/MAX11060.html?intcid=para

https://www.maximintegrated.com/en/products/analog/data-converters/analog-to-digital-converters/MAX11040KEVKIT.html

Resolution (bits) (ADC)		16
Input Channels		4
Conv. Rate (ksps) (max)		64
Data Bus			SPI
ADC Architecture		Sigma-Delta
Diff/S.E. Input	Diff. Only
Internal VREF (V) (nominal)	2.5
External VREF (V) (min)		2.3
External VREF (V) (max)		2.7
Bipolar VIN (±V) (max)		2.2

Teensy 4.0 and audio shield: 

https://www.adafruit.com/product/4323

https://www.adafruit.com/product/4384

ARM Cortex-M7 at 600 MHz
1024K RAM (512K is tightly coupled)
2048K Flash (64K reserved for recovery & EEPROM emulation)
2 USB ports, both 480 MBit/sec
3 CAN Bus (1 with CAN FD)
2 I2S Digital Audio
1 S/PDIF Digital Audio
1 SDIO (4 bit) native SD
3 SPI, all with 16 word FIFO
3 I2C, all with 4 byte FIFO
7 Serial, all with 4 byte FIFO
32 general purpose DMA channels
31 PWM pins
40 digital pins, all interrrupt capable
14 analog pins, 2 ADCs on chip
Cryptographic Acceleration
Random Number Generator
RTC for date/time
Programmable FlexIO
Pixel Processing Pipeline
Peripheral cross triggering
Power On/Off management
high quality 16 bit, 44.1 kHz sample rate (From audioshield)
