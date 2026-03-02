"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
Project1 Spring 2
File: room_booking.py
Purpose: This file handles the room booking logic
"""

import os
import json
import requests
from dotenv import load_dotenv
from handle_request_decorator import handle_request_exceptions


class RoomBooking:
    """
    RoomBooking class which contains all methods necessary for Spring 2
    """

    def __init__(self):
        """
        Initiate by loading the necessary data and set the constant API,
        followed by declaring the tokens that will later be used
        """
        load_dotenv(override=False)
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        server_address = os.getenv("SERVER_ADDRESS")
        server_port = os.getenv("SERVER_PORT")
        self.api = f"{server_address}:{server_port}/"
        self.authentication_status_code = None
        self.headers = None

    @handle_request_exceptions
    def authenticate(self) -> None:
        """
        METHOD: POST
        login at the endpoint 'api/v1/member/login/ '
        returns the access token and refresh token
        :return: None
        """
        endpoint = "api/v1/member/login/"
        user_credentials = {
            "email": self.email,
            "password": self.password
        }
        response = requests.post(f"{self.api}{endpoint}", json=user_credentials, timeout=10)
        self.authentication_status_code = response.status_code
        # self.refresh_token = response.json()['token']['refresh']
        access_token = response.json()['token']['access']
        self.headers = {"Authorization": f"Bearer {access_token}"}

    @handle_request_exceptions
    def get_available_meeting_rooms(self) -> json:
        """
        METHOD: GET
        Objective: Get the available meeting rooms
        :return: json
        """
        endpoint = "/api/v1/meeting-rooms/available/"

        rooms = requests.get(f"{self.api}/{endpoint}", headers=self.headers, timeout=10)
        return rooms.json()

    @handle_request_exceptions
    def book_a_meeting_room(self, room_id: int, start_time: str, end_time: str) -> json or None:
        """
        METHOD: POST
        Objective: book a meeting only if there is booking space
        :return: json
        """
        endpoint = f"{self.api}/api/v1/meeting-rooms/{room_id}/book/"
        booking_time = {
            "start_time": start_time,
            "end_time": end_time,
        }
        response = requests.post(endpoint, headers=self.headers, json=booking_time, timeout=10)
        print(response.json())
        return response.json()

    @handle_request_exceptions
    def list_my_bookings(self) -> json or None:
        """
        METHOD: GET
        Returns all my bookings
        :return:
        """
        endpoint = f"{self.api}/api/v1/meeting-rooms/my-bookings/"
        response = requests.get(endpoint, headers=self.headers, timeout=10)
        return response.json()

    @handle_request_exceptions
    def cancel_meeting_room(self, booking_id: int) -> json or None:
        """
        METHOD: DELETE
        Objective: cancel a booking based on the id
        :param booking_id:
        :return: json or None
        """
        endpoint = f"{self.api}/api/v1/meeting-rooms/{booking_id}/cancel-booking/"
        response = requests.delete(endpoint, headers=self.headers, timeout=10)
        if response.status_code == 204:
            return {"success": True}
        if response.text:
            return response.json()
        return {"status_code": response.status_code}
