# Noise Cleaning focused on: RNNoise and Krisp.ai
In addition:
I added instructions for how to test both noise cleaning softwares 
How to use Deepspeech
How to link Deepspeech and RNNoise to a gstreamer pipeline (should you want to)

Note: Cannot add deepspeech, rnnoise, or Krisp due to size. The audio files were run though the noise cleaning software, 
but the cleaned files can be found in the shared NASA EV3 Raiti folder

## For RNNoise:
from:
https://github.com/xiph/rnnoise

To compile, just type:
% ./autogen.sh
% ./configure
% make

May need to download required dependencies that default debian 10 does not have...
However the Rpi I made will already have everything needed

Input and output are RAW 16-bit (machine endian) mono PCM files sampled at 48 kHz

run program with 
./examples/rnnoise_demo <number of channels> <maximum attenuation> < input.raw > output.raw

Rnnoise also runs as part of a gstreamer pipeline...
You will need Rust and Docker (cargo) for this


## For Krisp.ai:
There is a free version for PC and Mac
Can test using audacity, play sound file into microphone > change microphone to Krisp.ai microphone
(there is no command line interface)


## For Deepspeech:
This is a demonstration of deepspeech's realtime transcription
from:
https://github.com/mozilla/DeepSpeech/releases

Need:
deepspeech-0.8.2-models.pbmm
deepspeech-0.8.2-models.scorer

these are the models you will need for the below example

from:
https://github.com/mozilla/DeepSpeech-examples/tree/r0.8/mic_vad_streaming

clone folder
Install dependencies

run example .py code

Deepspeech can also be run with Gstreamer, as part of a gstreamer pipeline:
https://github.com/Elleo/gst-deepspeech



