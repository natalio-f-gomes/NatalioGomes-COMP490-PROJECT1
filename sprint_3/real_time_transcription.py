"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: real_time_transcription.py
Purpose: Contains the logic of getting audio and getting transcript while he user is speaking
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
from ai_execution_handler import FilterLogic


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
        self.exit_command = "terminate"
        self.execution_command = "execute"
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
        os.makedirs(f"recording/{current_time}", exist_ok=True)
        audio_location = f"recording/{current_time}/audio.wav"
        write(audio_location, get_sample_rate(), recording)
        duration = (len(recording) / get_sample_rate())
        print(f"Audio saved to {audio_location}. Duration: {duration:.3f} seconds")
        return audio_location

    def print_instructions(self) -> str:
        """
        Returns the instructions for the CLI
        :return: str
        """
        return (f"{"="*50}RECORDING{"="*50}\n "
                f"PLEASE SPEAK CLEARLY IN THE MICROPHONE\n"
                f"(SAY THE COMMAND: '{self.execution_command}' to EXECUTE A QUERY)\n"
                f"(SAY THE COMMAND: '{self.exit_command}' to STOP)\n")

    def put_recording_blocks_together(self, audio_blocks: list[numpy.ndarray]) \
            -> numpy.ndarray or None:
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

    def execute_user_prompt(self) -> None:
        """
        Responsible for calling claude AI and give sit the user prompt.
        :return: None
        """

        instance = FilterLogic()
        user_prompt = json.loads(self.recognizer.FinalResult())
        user_prompt = user_prompt.get("text", "")
        if user_prompt:
            print(f"User Prompt:\t{user_prompt}")
            self.all_transcriptions.append(user_prompt)

        full_user_query = " ".join(self.all_transcriptions)
        full_user_query = full_user_query[:full_user_query.rfind(self.execution_command)].strip()
        full_user_query = full_user_query.replace(self.execution_command, "")
        instance.call_claude_ai(full_user_query)

    def close_audio_capture(self, audio_stream: object, audio_blocks: list[numpy.ndarray],
                            exit_program: bool) -> None:
        """
        Either when the user says the exit command or kills the program abruptly
        this method is called it gathers the final pieces.
        :param audio_stream: object
        :param audio_blocks: list[numpy.ndarray]
        :param exit_program: bool
        :return: None
        """
        audio_stream.stop()
        audio_stream.close()
        # Grab any remaining text the recognizer hasn't finalized
        final = json.loads(self.recognizer.FinalResult())
        final_text = final.get("text", "")
        if final_text:
            print(f"Transcript:   {final_text}")
            self.all_transcriptions.append(final_text)
        if exit_program:
            self.put_recording_blocks_together(audio_blocks)

    def record(self) -> str:
        """
        Opens an audio stream, reads blocks from the queue,
        and feeds them directly into the Vosk recognizer.
        Finally, it prints the transcription
        Unfortunately, I am not sure how to test this method yet
        """
        audio_stream = sounddevice.InputStream(
            samplerate=get_sample_rate(),
            channels=get_channel(),
            dtype=get_d_type(),
            callback=self.put_audio_in_the_queue,
            blocksize=1024,
        )
        audio_blocks = []
        exit_program = False
        try:
            print(self.print_instructions())
            audio_stream.start()
            while exit_program is not True:
                try:
                    # Get the next audio block from the queue.
                    # Wait for the data to arrive for 0.2 seconds
                    data = self.audio_queue.get(timeout=0.2)
                    audio_blocks.append(data)
                    audio_bytes = data.tobytes()

                    if self.recognizer.AcceptWaveform(audio_bytes):
                        result = json.loads(self.recognizer.Result())
                        text = result.get("text", "")
                        if self.exit_command in text:
                            exit_program = True
                        if text:
                            print(f"Transcript:   {text}")
                            self.all_transcriptions.append(text)
                        if self.execution_command in text:
                            self.execute_user_prompt()
                    else:
                        partial = json.loads(self.recognizer.PartialResult())
                        partial_text = partial.get("partial", "")
                        if self.exit_command in partial_text:
                            exit_program = True
                        if partial_text:
                            print(f"Transcript: {partial_text}", end="\r")
                        if self.execution_command in partial_text:
                            self.execute_user_prompt()
                except queue.Empty:
                    # No audio in queue, just continue waiting
                    pass
        except KeyboardInterrupt:
            print("\n\nStopping...")
            self.close_audio_capture(audio_stream, audio_blocks, exit_program)
        finally:
            self.close_audio_capture(audio_stream, audio_blocks, exit_program)

        full_transcription = " ".join(self.all_transcriptions)
        full_transcription = full_transcription.replace(self.exit_command, " ")
        return full_transcription
