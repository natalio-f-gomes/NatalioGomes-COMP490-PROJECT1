"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: test_audio_transcription.py
Purpose: Test Methods of the test_audio_transcription class
"""

import os

from audio_transcription import transcribe_audio

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


class TestAudioTranscription:
    """
    Class that contains methods that tests the individual methods of audio_transcription.py
   """

    def test_transcribe_audio(self):
        """
        tests if the transcripts actually match the words of the audio
        :return: None
        """
        audio_1_path = os.path.join(TEST_DIR, "test_recording", "2026-02-01 14:04:28.974366", "audio.wav")
        transcription_1 = transcribe_audio(audio_1_path)

        audio_2_path = os.path.join(TEST_DIR, "test_recording", "2026-02-01 14:09:04.124898", "audio.wav")
        transcription_2 = transcribe_audio(audio_2_path)

        assert transcription_1 == "hello world"
        assert transcription_2 == "john week is the best movie franchise ever made"

    def test_write_transcription_to_a_file(self):
        """
        tests if the content of the file match the correct output
        :return: None
        """
        transcription_path_1 = os.path.join(TEST_DIR, "test_recording", "2026-02-01 14:04:28.974366", "transcription"
                                                                                                      ".txt")

        with open(transcription_path_1, "r", encoding='utf-8') as file:
            content = file.read()
            assert content == "hello world"
