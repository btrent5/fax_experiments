#!/usr/bin/python
# based on : www.daniweb.com/code/snippet263775.html
# based on: https://stackoverflow.com/questions/33879523/python-how-can-i-generate-a-wav-file-with-beeps

import math
import wave
import struct
from random import random

sample_rate = 9600


def append_silence(audio=[], duration_milliseconds=500):
    """
    Adding silence is easy - we add zeros to the end of our array
    """
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(0.0)

    return


def save_wav(audio=[], file_name=''):
    # Open up a wav file
    wav_file = wave.open(file_name, "w")

    # wav params
    nchannels = 1

    sampwidth = 2

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate,
                        nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))

    wav_file.close()

    return


def append_sinewave(audio=[],
                    freq=440.0,
                    duration_milliseconds=500,
                    volume=1.0):

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * (x / sample_rate)))

    return


audio = []

# # sample beep routine
# append_sinewave(audio, volume=0.5)
# append_silence(audio)
# append_sinewave(audio, volume=0.5)
# append_silence(audio)
# append_sinewave(audio, volume=0.5)

# sample 01010101010 routing
for i in range(100):
    if random() > 0.5:
        append_sinewave(audio, freq=1000, duration_milliseconds=30, volume=0.5)
    else:
        append_sinewave(audio, freq=500, duration_milliseconds=30, volume=0.5)


save_wav(audio, "output.wav")
