"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: audio_transcription.py
Purpose: This file handles the transcription of audio using local vosk api
"""

import json
import wave

from vosk import Model, KaldiRecognizer


def transcribe_audio(audio_location:str) -> str:
    """
    Reference: https://github.com/alphacep/vosk-api/blob/master/python/example/test_simple.py
    :param audio_location:
    :return: transcription
    Loop through the transcription while its translating and appends it to a list.
    Later on adds the final result to the list and concatenates the
        item inside the list and return the final result
    """
    wave_frame = wave.open(audio_location, "rb")
    model = Model(lang="en-us")

    recognizer = KaldiRecognizer(model, wave_frame.getframerate())
    print(f"Framerate {wave_frame.getframerate()}")
    recognizer.SetWords(True)
    recognizer.SetPartialWords(False)

    all_transcriptions = []

    while True:
        data = wave_frame.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            transcription = json.loads(recognizer.Result())
            if transcription.get("text"):
                all_transcriptions.append(transcription["text"])

    final_result = json.loads(recognizer.FinalResult())

    if final_result.get("text"):
        all_transcriptions.append(final_result["text"])

    full_transcription = " ".join(all_transcriptions)

    wave_frame.close()

    return full_transcription


def write_transcription_to_a_file(transcription: str, audio_file_path: str) -> None:
    """
    :param transcription:
    :param audio_file_path:
    :return: None
    removes the "audio.wav" from the file path and adds transcription
    """
    audio_file_path = audio_file_path[:-9] + "transcription.txt"
    with open(audio_file_path, "w", encoding='utf-8') as file:
        file.write(transcription)
