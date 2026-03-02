"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: app.py
Purpose: Puts everything together
"""

from real_time_transcription import RealTimeTranscription


if __name__ == "__main__":
    transcriber = RealTimeTranscription()
    TRANSCRIPTION = transcriber.record()
    print(f"\n--------- Full Transcription ---------\n{TRANSCRIPTION}")
