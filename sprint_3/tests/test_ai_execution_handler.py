"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: test_ai_execution_handler.py
Purpose: This file tests the methods of the ai_execution_handler.py file
"""

import os
import random
from ai_execution_handler import FilterLogic
from room_booking import RoomBooking
from audio_transcription import transcribe_audio

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


class TestAIExecutionHandler:
    """
    Tests the required methods of sprint 3
    """
    def test_filter_booking(self):
        """ Checks if the filtering of bookings is working"""
        filter_instance = FilterLogic()
        all_bookings_before_filtering = filter_instance.all_my_bookings
        assert all_bookings_before_filtering is not None
        random_booking = all_bookings_before_filtering[random.randint(0, len(all_bookings_before_filtering) - 1)]
        filter_instance.filter_booking('id', random_booking['id'])
        bookings_after_filtering = filter_instance.all_my_bookings
        assert bookings_after_filtering is not None
        assert bookings_after_filtering[0]['id'] ==  random_booking['id']
        assert bookings_after_filtering[0]['meeting_room']['id'] == random_booking['meeting_room']['id']
        assert bookings_after_filtering[0]['meeting_room']['room_name'] == random_booking['meeting_room']['room_name']
        assert bookings_after_filtering[0]['meeting_room']['capacity'] == random_booking['meeting_room']['capacity']
        assert isinstance(bookings_after_filtering[0]['meeting_room']['capacity'], int)

    def test_filter_room(self):
        """ Checks if the filtering of room is working"""
        filter_instance = FilterLogic()
        all_bookings_before_filter = filter_instance.all_my_bookings
        assert all_bookings_before_filter is not None
        filter_instance.filter_room('room_name', 'Room A')
        all_bookings_after_filter = filter_instance.all_my_bookings
        assert all_bookings_after_filter is not None
        for booking in all_bookings_after_filter:
            assert booking['meeting_room']['capacity'] == 4
            assert booking['meeting_room']['capacity'] != '4'

    def test_filter_by_ai_data_with_valid_data(self):
        """ Feeds the AI a valid prompt and asserts the result with a predetermined conclusion """
        filter_instance = FilterLogic()
        all_bookings_before_filtering = filter_instance.all_my_bookings
        assert all_bookings_before_filtering is not None
        test_data = {'room_name': 'Room B'}
        filter_instance.filter_by_ai_data(test_data)
        all_bookings_after_filtering = filter_instance.all_my_bookings
        assert all_bookings_after_filtering is not None
        assert len(all_bookings_after_filtering) > 1

    def test_filter_by_ai_data_with_invalid_data(self):
        """ Feeds the AI an invalid prompt and checks the list of bookings which should be empty"""
        room_booking_instance = RoomBooking()
        room_booking_instance.authenticate()
        filter_instance = FilterLogic()
        all_bookings_before_filtering = filter_instance.all_my_bookings
        assert all_bookings_before_filtering is not None
        test_data = {'room_name': 'Room ZYZ'}
        filter_instance.filter_by_ai_data(test_data)
        all_bookings_after_filtering = filter_instance.all_my_bookings
        assert all_bookings_after_filtering == []

    def test_get_content(self):
        """Checks if the function get_content is returning instructions for ai"""
        filter_instance = FilterLogic()
        assert filter_instance.get_content() is not None

    def test_clean_json_response(self):
        """Feeds a bunch of raw messages to  the clean_json_response to
        check if it is in fact stripping away the necessary strings"""
        filter_instance = FilterLogic()
        raw_message_1 = """```json{"list_all_bookings": "true"}```"""
        raw_message_2 = """"```json{"booking_id": "5"}```"""
        raw_message_3 = """"```json{"room_id": "3"}```"""
        raw_message_4 = """"```json{"room_name": "Room C"}```"""
        raw_message_5 = """"```json{"capacity": "20"}```"""
        raw_message_7 = """"```python{"capacity": "23"}```"""
        clean_message_1 = filter_instance.clean_json_response(raw_message_1)
        clean_message_2 = filter_instance.clean_json_response(raw_message_2)
        clean_message_3 = filter_instance.clean_json_response(raw_message_3)
        clean_message_4 = filter_instance.clean_json_response(raw_message_4)
        clean_message_5 = filter_instance.clean_json_response(raw_message_5)
        clean_message_7 = filter_instance.clean_json_response(raw_message_7)
        assert clean_message_1 == """{"list_all_bookings": "true"}"""
        assert clean_message_2 == """{"booking_id": "5"}"""
        assert clean_message_3 == """{"room_id": "3"}"""
        assert clean_message_4 == """{"room_name": "Room C"}"""
        assert clean_message_5 == """{"capacity": "20"}"""
        assert clean_message_7 == """{"capacity": "23"}"""

    def test_call_claude_ai_with_valid_prompt(self):
        """
        Passes valid prompt to AI and asserts its behavior
        :return:
        """
        filter_instance = FilterLogic()
        valid_prompt = "give me the bookings with the room name of dmf four seven three"
        msg = filter_instance.call_claude_ai(valid_prompt)
        assert msg == {'room_name': 'DMF 473'}

    def test_call_claude_ai_with_invalid_room_name(self):
        """ Passes an invalid prompt to AI and then checks
        the list of bookings which should be empty"""
        filter_instance = FilterLogic()
        invalid_prompt = "give me the bookings with the room name of Albeta"
        response = filter_instance.call_claude_ai(invalid_prompt)
        assert response == {'room_name': 'INVALID_ROOM_NAME'}

    def test_call_claude_ai_with_empty_prompt(self):
        """Passes an empty prompt to AI to raise a ValueError"""
        filter_instance = FilterLogic()
        assert filter_instance.call_claude_ai("") == {}

    def test_get_all_reservations_from_audio(self):
        """
        tests if the transcripts actually match the words of the audio
        :return: None
        """
        audio_1_path = os.path.join(TEST_DIR, "test_recording", "2026_02_21_15_07_11_220388",
                                    "audio.wav")
        transcription = transcribe_audio(audio_1_path)
        assert transcription == ("good all my reservations for the "
                                 "rome two zero six execute terminate")
        filter_instance = FilterLogic()
        filter_instance.call_claude_ai(transcription)
        assert filter_instance.all_my_bookings is not None

    def test_get_reservations_from_audio_with_invalid_booking(self):
        """
        tests if the transcripts actually match the words of the audio with an invalid command
        :return: None
        """
        audio_path = os.path.join(TEST_DIR, "test_recording", "2026_02_21_15_15_37_006809",
                                    "audio.wav")
        transcription = transcribe_audio(audio_path)
        assert transcription == "get my booking with the idea of ten thousand execute terminate"
        filter_instance = FilterLogic()
        response = filter_instance.call_claude_ai(transcription)
        assert response == {}


