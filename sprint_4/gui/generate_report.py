"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: generate_report.py
Purpose: This file generates report to the user whom booking was canceled
"""

import os
import csv
from datetime import datetime


class GenerateReport:
    def __init__(self):
        self.all_reports = []

    def write_report_to_csv(self):
        header = ["User ID", "Email", "Username", "Date", "Action", "Room ID", "Reservation IDs Canceled", "Total Reservations Canceled"]

        file_exists = os.path.exists("report.csv")

        with open('report.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if file_exists:
                writer.writerows(self.all_reports)
            else:
                writer.writerow(header)
                writer.writerows(self.all_reports)
            self.all_reports = []


    def get_user_booking_data(self, bookings_with_the_room_id: list[tuple]):
        user_booking_data = {}
        for i in bookings_with_the_room_id:
            if i[4] in user_booking_data:
                user_booking_data[i[4]] += 1
            else:
                user_booking_data[i[4]] = 1
        return user_booking_data

    def generate_report(self, date_of_action: datetime, action_type: str, users_affected: set[tuple], bookings_with_the_room_id: list[tuple] ,user_booking_data):
        data = self.get_user_booking_data(bookings_with_the_room_id)
        print(f"DEBUG: Bookings with the room id {bookings_with_the_room_id}")
        room_id = bookings_with_the_room_id[0][5]
        for user_data in users_affected:
            print(user_data)
            user_id = user_data[0]
            user_email = user_data[3]
            username = user_data[7]
            reservation_ids = []
            for i in  user_booking_data[user_id]:
                reservation_ids.append(i[0])
            print(f"reservation_ids {reservation_ids}")
            print(f"DEBUG: User ID: {user_id} Username: {username} User_email: {user_email} action_type: {action_type} Reservation_ids: {reservation_ids} Reservations Canceled: {data[user_id]}")
            report_data = (user_id, user_email, username,date_of_action,  action_type, room_id, reservation_ids, data[user_id])
            self.all_reports.append(report_data)
        self.write_report_to_csv()
