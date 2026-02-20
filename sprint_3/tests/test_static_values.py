"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: test_static_values.py
Purpose: Test Methods of the STATIC_VALUES FILE
"""
from static_values import get_channel, get_sample_rate, get_d_type


def test_get_sample_rate():
    """
    This function must always return a static value.
    Because of vosk api, it must be 16000
    :return: None
    """
    assert get_sample_rate() == 16000


def test_get_channel():
    """
    Assert that get channel is returning 1 for mono
    :return: None
    """
    assert get_channel() == 1


def test_get_d_type():
    """
    Assert that get_d_type is returning 'int16'
    :return:
    """
    assert get_d_type() == 'int16'
