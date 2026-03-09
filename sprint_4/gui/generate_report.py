"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: generate_report.py
Purpose: This file generates report to the user whom booking was affected
"""

import os
import csv
from datetime import datetime


class GenerateReport:
    """Generate Report Class"""
    def __init__(self):
        """Initialize constructor with all_reports list"""
        self.all_reports = []

    def write_report_to_csv(self) -> None:
        """Checks if the file exists and if it's not empty, create it and write the data from all reports to it"""
        header = ["User ID", "Email", "Username", "Date", "Action", "Room ID", "Reservation IDs Affected",
                  "Total Reservations Affected"]

        try:
            file_path = "Report/report.csv"
            file_exists = os.path.isfile(file_path) and os.path.getsize(file_path) > 0
            with open(file_path, 'a', newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                if file_exists:
                    writer.writerows(self.all_reports)
                else:
                    writer.writerow(header)
                    writer.writerows(self.all_reports)
                self.all_reports = []
        except FileNotFoundError:
            print("FILE NOT FOUND")


    @staticmethod
    def get_user_booking_data(bookings_with_the_room_id: list[tuple]) -> dict:
        """Get the user booking data from the user booking list, use a dictionary to store
         user id and the amount of bookings"""
        user_booking_data = {}
        for i in bookings_with_the_room_id:
            if i[4] in user_booking_data:
                user_booking_data[i[4]] += 1
            else:
                user_booking_data[i[4]] = 1
        return user_booking_data

    def generate_report(self, action_type: str, users_affected: set[tuple],
                        bookings_with_the_room_id: list[tuple] ,user_booking_data: dict) -> None:
        """
        Grabs the data, loops through it, takes the relevant data and adds it to the all_reports list
        and then calls the write_report_to_csv method
        :param date_of_action: datetime
        :param action_type: str
        :param users_affected: set[tuple]
        :param bookings_with_the_room_id:  list[tuple]
        :param user_booking_data: dict
        :return: None
        """
        date_of_action = datetime.now()
        data = self.get_user_booking_data(bookings_with_the_room_id)
        print(f"DEBUG: Bookings with the room id {bookings_with_the_room_id}")
        room_id = bookings_with_the_room_id[0][5]
        print(f"DEBUG: Room ID: {room_id}")
        for user_data in users_affected:
            print(user_data)
            user_id = user_data[0]
            user_email = user_data[3]
            username = user_data[7]
            reservation_ids = []
            for i in  user_booking_data[user_id]:
                reservation_ids.append(i[0])
            print(f"DEBUG: User ID: {user_id} Username: {username} User_email: {user_email} action_type:"
                  f" {action_type} Reservation_ids: {reservation_ids} Reservations Canceled: {data[user_id]}")
            report_data = (user_id, user_email, username,date_of_action,  action_type, room_id, reservation_ids, data[user_id])
            self.all_reports.append(report_data)
        self.write_report_to_csv()
