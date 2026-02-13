"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
Project1 Spring 2
File: display_data.py
Purpose: This file contains the 'DisplayDataInTerminal' class that has the methods
that test the "RoomBooking's" methods
"""

import random
import json
from datetime import datetime
from random import randrange
from room_booking import RoomBooking


class DisplayDataInTerminal:
    """
    DisplayDataInTerminal class
    """

    def __init__(self):
        """
        Initiate Instance by authenticating and Getting the available rooms
        """
        self.instance = RoomBooking()
        self.instance.authenticate()
        self.total_available_rooms = 0
        self.all_my_booking_ids = []
        self.available_rooms = self.instance.get_available_meeting_rooms()
        for _ in self.instance.get_available_meeting_rooms():
            self.total_available_rooms += 1

    @staticmethod
    def display_individual_room_information(room: json):
        """
        Receives the room dictionary and then print the information in each lne
        :param room: json
        :return: None
        """
        print(f"Room id: {room['id']}")
        print(f"Room Name: {room['room_name']}")
        print(f"Room Capacity: {room['capacity']}")

    @staticmethod
    def is_leap_year(year: int):
        """
        Calculates leap year
        :param year:
        :return:
        """
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    def generate_a_random_booking_time(self):
        """
        Gets a random year, and month
        Based on the year and month, it will get a random day.
        The day cannot be over 28 if the year is lead and the month is february
        Does string formatting and at the end, returns start time and end time
        :return: None
        """
        rand_year = randrange(datetime.now().year + 1, datetime.now().year + 10)
        rand_month = randrange(1, 12)
        if self.is_leap_year(rand_year) and rand_month == 2:
            rand_day = randrange(1, 28)
        else:
            rand_day = randrange(1, 31)
        rand_hour = randrange(0, 23)
        valid_minutes = list(range(0, 60, 15))
        random_minute = random.choice(valid_minutes)
        start_time_str = f"{rand_hour}:{random_minute}:00"
        start_time_object = datetime.strptime(start_time_str, "%H:%M:%S")
        start_time_str_formatted = start_time_object.strftime("%I:%M %p")
        if random_minute == 45:
            end_time_str = f"{rand_hour + 1}:00:00"
        else:
            end_time_str = f"{rand_hour}:{random_minute + 15}:00"
        end_time_object = datetime.strptime(end_time_str, "%H:%M:%S")
        end_time_str_formatted = end_time_object.strftime("%I:%M %p")

        start_datetime = f"{rand_year}-{rand_month:02d}-{rand_day:02d} {start_time_str_formatted}"
        end_datetime = f"{rand_year}-{rand_month:02d}-{rand_day:02d} {end_time_str_formatted}"

        assert start_datetime is not None
        assert end_datetime is not None
        return start_datetime, end_datetime

    def display_available_rooms(self):

        """
        Displays all my available Rooms
        :return: None
        """
        print(f"{'=' * 62} Available rooms {'=' * 62}")
        for room in self.available_rooms:
            print(room)

    def book_random_meeting_room(self):
        """
        Picks a random meeting room and books it
        :return:
        """
        random_number = random.randrange(self.total_available_rooms)
        random_room = self.available_rooms[random_number]
        random_room_id = self.available_rooms[random_number]["id"]
        start_time, end_time = self.generate_a_random_booking_time()
        book_meeting_room = self.instance.book_a_meeting_room(random_room_id, start_time, end_time)
        print("Booking a meeting room...")
        self.display_individual_room_information(random_room)
        print(f"Book a Meeting Room Response: {book_meeting_room}")

    def display_all_my_booking(self):
        """
        Displays all my bookings
        :return: None
        """
        print(f"{'=' * 62} All My Bookings {'=' * 62}")
        all_bookings = self.instance.list_my_bookings()
        for booking in all_bookings:
            self.all_my_booking_ids.append(booking['id'])
            print(booking)

    def cancel_all_bookings(self):
        """"
        Loops though my bookings and cancels them
        :return: None
        """
        errors = 0
        reason = ""
        success = 0
        for booking_id in self.all_my_booking_ids:
            cancel_booking_response = self.instance.cancel_meeting_room(booking_id)
            print(f"Attempt to cancel booking with id {booking_id}."
                  f" Response: {cancel_booking_response}")
            try:
                if cancel_booking_response['error']:
                    errors += 1
                    reason = cancel_booking_response['error']
            except KeyError:
                if cancel_booking_response['success']:
                    success += 1
        print(f"{errors} bookings could not be canceled because of:"
              f" '{reason}'.\n"
              f"{success} of your bookings has been successfully canceled")

    def cancel_a_random_booking(self):
        """
        For test purposes, this method exists for canceling a random booking room
        :return: None
        """
        print(f"{'=' * 62} Cancel a Random Booking {'=' * 62}")
        random_booking_id = random.choice(self.all_my_booking_ids)
        print(f"Booking id to be canceled: {random_booking_id}")
        cancel_booking_response = self.instance.cancel_meeting_room(random_booking_id)
        try:
            if cancel_booking_response["success"]:
                print(f"Successfully Canceled the booking with id: {random_booking_id}")
            else:
                print(f"{cancel_booking_response}")
        except KeyError as e:
            print(e)

    def book_n_meeting_rooms(self, n: int):
        """
        Books n amount of rooms
        :param n:
        :return: None
        """
        for _ in range(n):
            self.book_random_meeting_room()
