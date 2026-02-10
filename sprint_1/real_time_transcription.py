"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: real_time_transcription.py
Purpose: Contains the logic of getting audio and getting transcript while he user is speaking
TODO: Write unit tests for recording method
    Make Sure to change the test do it gest the correct folder(without the ":")
"""

import json
import os
import queue
from datetime import datetime
import numpy
from scipy.io.wavfile import write
import sounddevice
from vosk import Model, KaldiRecognizer
from static_values import get_channel, get_sample_rate, get_d_type
from audio_transcription import transcribe_audio, write_transcription_to_a_file


class RealTimeTranscription:
    """
    Captures audio from the microphone and transcribes it in real-time
    using Vosk offline api.
    """

    def __init__(self):
        """
        Initialize the class with the necessary fields.
        """
        self.audio_queue = queue.Queue()
        self.model = Model(lang="en-us")
        self.recognizer = KaldiRecognizer(self.model, get_sample_rate())
        self.recognizer.SetWords(True)
        self.recognizer.SetPartialWords(False)
        self.exit_command = "exit the program"
        self.exit_program = False
        self.audio_stream = sounddevice.InputStream(
            samplerate=get_sample_rate(),
            channels=get_channel(),
            dtype=get_d_type(),
            callback=self.put_audio_in_the_queue,
            blocksize=1024,
        )
        self.all_transcriptions = []

    def put_audio_in_the_queue(
            self,
            input_data: numpy.ndarray,
            frames: int,
            time: object,
            status: sounddevice.CallbackFlags,
    ) -> None:
        """
        Callback for sounddevice InputStream.
        Adds a copy of each audio block to the queue.
        It needs all 4 parameters, otherwise it will not work.
        """
        if status:
            print(f"Status: {status}")
        self.audio_queue.put(input_data.copy())

    @staticmethod
    def get_audio_location(recording: numpy.ndarray,
                           current_time: datetime = datetime.now()) -> str or None:
        """
        :param current_time:
        :param recording:
        :return: None
        Put the data together, save it to the audio file and return the audio directory
        """
        if recording is None:
            print("Cannot save: recording data is NONE")
            return None
        current_time = (str(current_time).replace(":", "_")
                        .replace(".", "_").replace("-", "_"))
        os.makedirs(f"recording/{current_time}", exist_ok=True)
        audio_location = f"recording/{current_time}/audio.wav"
        write(audio_location, get_sample_rate(), recording)
        duration = (len(recording) / get_sample_rate())
        print(f"Audio saved to {audio_location}. Duration: {duration:.3f} seconds")
        return audio_location

    def put_recording_blocks_together(self, audio_blocks: list[numpy.ndarray]) -> numpy.ndarray or None:
        """
        :param audio_blocks
        :return: the audio block
        """
        if audio_blocks:
            recording = numpy.concatenate(audio_blocks, axis=0)
            print(f"recording {recording}")
            audio_location = self.get_audio_location(recording)
            transcript = transcribe_audio(audio_location)
            transcript = transcript.replace(self.exit_command, "")
            write_transcription_to_a_file(transcript, audio_location)
            return recording
        print("No Audio Was Recorded")
        return None

    def stop_the_program(self, audio_blocks):
        """
        Responsible for putting audio and transcription together
            and stop the audio_stream
        :return: None
        """
        self.audio_stream.stop()
        self.audio_stream.close()

        # Grab any remaining text the recognizer hasn't finalized
        final = json.loads(self.recognizer.FinalResult())
        final_text = final.get("text", "")

        if final_text or self.exit_program:
            print(f"Transcript:   {final_text}")
            self.all_transcriptions.append(final_text)
            self.put_recording_blocks_together(audio_blocks)

    def record(self) -> str:
        """
        Opens an audio stream, reads blocks from the queue,
        and feeds them directly into the Vosk recognizer.
        Finally, it prints the transcription
        Unfortunately, I am not sure how to test this method yet
        """
        audio_blocks = []
        try:
            print(f"... RECORDING ...\n"
                  f"(SAY THE COMMAND: '{self.exit_command}' to STOP)\n")
            self.audio_stream.start()
            while self.exit_program is not True:
                try:
                    # Get the next audio block from the queue. Wait for the data to arrive for 0.2 seconds
                    data = self.audio_queue.get(timeout=0.2)
                    audio_blocks.append(data)
                    audio_bytes = data.tobytes()
                    if self.recognizer.AcceptWaveform(audio_bytes):
                        result = json.loads(self.recognizer.Result())
                        text = result.get("text", "")
                        if self.exit_command in text:
                            self.exit_program = True
                        if text:
                            print(f"Transcript:   {text}")
                            self.all_transcriptions.append(text)
                    else:
                        partial = json.loads(self.recognizer.PartialResult())
                        partial_text = partial.get("partial", "")
                        if self.exit_command in partial_text:
                            self.exit_program = True
                        if partial_text:
                            print(f"Transcript: {partial_text}", end="\r")
                except queue.Empty:
                    # No audio in queue, just continue waiting
                    pass

        except KeyboardInterrupt:
            print("\n\nStopping...")
            self.stop_the_program(audio_blocks)
        finally:
            self.stop_the_program(audio_blocks)
        full_transcription = " ".join(self.all_transcriptions)
        full_transcription = full_transcription.replace(self.exit_command, " ")
        return full_transcription
