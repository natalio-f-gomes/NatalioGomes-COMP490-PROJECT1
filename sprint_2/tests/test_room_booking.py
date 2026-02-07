"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
Project1 Spring 2
File: test_room_booking.py
Purpose: This file contains the class that tests 3 methods required for sprint-2
"""

import random
from room_booking import RoomBooking
from display_data import DisplayDataInTerminal


class TestRoomBooking:
    """
    Class: TestRoomBooking
    Contains the main unit tests of the RoomBooking class
    """
    def test_authentication(self):
        """
        Tests the authentication
        :return: None
        """
        room_booking_instance = RoomBooking()
        room_booking_instance.authenticate()
        assert room_booking_instance.authentication_status_code == 200

    def test_get_available_rooms(self):
        """
        Compares the manual available rooms with the ones returned by the API
        :return: None
        """
        room_booking_instance = RoomBooking()
        room_booking_instance.authenticate()
        available_rooms_from_api = room_booking_instance.get_available_meeting_rooms()
        available_rooms = [
            {'id': 1, 'room_name': 'Room A', 'capacity': 4},
            {'id': 2, 'room_name': 'Room B', 'capacity': 10},
            {'id': 3, 'room_name': 'Room C', 'capacity': 3},
            {'id': 4, 'room_name': 'DMF 473', 'capacity': 12},
            {'id': 5, 'room_name': 'DMF 471', 'capacity': 12},
            {'id': 6, 'room_name': 'DMF 363', 'capacity': 24},
            {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
            {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
            {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20}
        ]

        for api_room, available_room in zip(available_rooms_from_api, available_rooms):
            assert api_room == available_room

    def test_booking_a_room(self):
        """
        Test booking a room with a random id and random start time and end time twice
        The first time it is supposed to get an success response and the second time: an error
        :return: None
        """
        display_data_instance = DisplayDataInTerminal()
        room_booking_instance = RoomBooking()
        room_booking_instance.authenticate()
        random_id = random.choice(list(range(1, 10)))
        start_time, end_time = display_data_instance.generate_a_random_booking_time()
        response_msg_1 = room_booking_instance.book_a_meeting_room(random_id, start_time, end_time)
        response_msg_2 = room_booking_instance.book_a_meeting_room(random_id, start_time, end_time)
        success_message = 'Meeting room booked successfully.'
        failed_message = ("Meeting room is not available or does not have "
                          "sufficient capacity for the specified time range and number of persons.")
        if response_msg_1 is not None:
            assert response_msg_1["message"] == success_message
        if response_msg_2 is not None:
            assert response_msg_2["error"] == failed_message
        # clean up my bookings
        display_data_instance.cancel_all_bookings()
