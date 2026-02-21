"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: static_values.py
Purpose: Holds methods that return static values
"""


def get_sample_rate() -> int:
    """
    44 100 - this was the previous value given by online sources
    44 100 is the number of frequency that is normal for human hearing.

   Sample rate refers to how many times per second an analog signal is measured.
   Common rates include 44.1 kHz and 48 kHz.
   Source: https://www.izotope.com/en/learn/digital-audio-basics-sample-rate-and-bit-depth
   Vosk API requires a sample rate of 16 000
   :return: constant
   """
    return 16000


def get_channel() -> int:
    """
    1 for Mono -> 1 audio input source
    2 for Stereo -> 2 audio input sources
    :return:
    """
    return 1


def get_d_type() -> str:
    """
    int16 simply means how audio is stored in memory. 16 is 2 bytes.
    So 2^16 = 65, 536. This is for standard audio
    float32 is for mixing.
    :return:
    """
    return 'int16'
