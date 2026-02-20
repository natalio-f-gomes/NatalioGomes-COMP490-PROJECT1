"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: test_real_time_transcription.py
Purpose: Test Methods of the app.py file
"""
import datetime

import numpy
from numpy.testing import assert_array_equal

from app import RealTimeTranscription


class TestApp:
    """
    Test all methods of the RealTimeTranscription class
    """

    def test_vosk_model(self):
        """
        Test the RealTimeTranscription initialization
        :return: None
        """
        instance = RealTimeTranscription()
        audio_queue = instance.audio_queue
        assert audio_queue.full() is False
        assert audio_queue.empty() is True
        assert instance.exit_command == "exit the program"
        assert instance.recognizer.Result() == '{"text": ""}'

    def test_1d_array_add_audio_to_queue(self):
        """
        Testing adding 1 dimensional numpy array to the queue
        :return: None
        """
        audio_queue_instance = RealTimeTranscription().audio_queue
        input_data = numpy.array([1, 2, 3, 4, 5]).all()
        audio_queue_instance.put(input_data)
        assert_array_equal(audio_queue_instance.get(), input_data)

    def test_nd_array_add_audio_to_queue(self):
        """
        Testing adding n dimensional numpy array to the queue
        :return: None
        """
        audio_queue_instance = RealTimeTranscription().audio_queue
        input_data = numpy.array([[1, 2, 3], [9, 0, 8], [1, 2, 3]])
        audio_queue_instance.put(input_data)
        assert_array_equal(audio_queue_instance.get(), input_data)

    def test_put_recording_blocks_together(self):
        """
        Testing the concatenation of recording block
        :return: None
        """
        fake_recording_block = []
        array1 = numpy.array([0, 1, 2])
        array2 = numpy.array([0, 3, 2])
        array3 = numpy.array([2, 3, 2])
        fake_recording_block.append(array1.copy())
        fake_recording_block.append(array2.copy())
        fake_recording_block.append(array3.copy())
        instance = RealTimeTranscription()
        result = instance.put_recording_blocks_together(fake_recording_block)
        array_final = numpy.concatenate(fake_recording_block)
        assert_array_equal(array_final, result)

    def test_get_file_name(self):
        """
        Testing is the audio file is created
        return: None
        """
        fake_recording_block = []
        array1 = numpy.array([0, 1, 2])
        array2 = numpy.array([0, 3, 2])
        fake_recording_block.append(array1.copy())
        fake_recording_block.append(array2.copy())
        array_final = numpy.concatenate(fake_recording_block)
        fake_time = datetime.datetime(2025, 6, 15, 14, 35, 22)
        instance = RealTimeTranscription()
        filename = instance.get_audio_location(array_final, fake_time)
        assert filename == f"recording/{fake_time}/audio.wav"
