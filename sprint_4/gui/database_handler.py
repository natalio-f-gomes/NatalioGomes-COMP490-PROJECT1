"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: database_handler.py
Purpose: This file handles Database CRUD functionalities
"""


import sqlite3
from generate_report import GenerateReport

class DatabaseHandler:
    """Database Handler Class with all necessary methods for sprint_4"""
    def __init__(self, connection=None):
        """Initialize the constructor by loading the db"""
        if connection is not None:
            self.connection = connection
        else:
            self.database_path = 'db.sqlite3'
            self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        self.generate_report = GenerateReport()

    def get_all_rooms(self) -> list[tuple]:
        """Get all rooms"""
        command = """SELECT * FROM booking_meetingroom"""
        return self.cursor.execute(command).fetchall()

    def get_user_by_id(self, user_id: int) -> tuple:
        """Get room by ID"""
        sql = "SELECT * FROM member_customuser WHERE id = ?"
        return self.cursor.execute(sql, (user_id,)).fetchone()

    def get_booking_by_id(self, booking_id: int) -> list[tuple]:
        """Get room by ID"""
        sql = "SELECT * FROM booking_bookinghistory WHERE id = ?"
        return self.cursor.execute(sql, (booking_id,)).fetchall()

    def get_booking_by_room_id(self, room_id: int) -> list[tuple]:
        """Get room by ID"""
        sql = "SELECT * FROM booking_bookinghistory WHERE meeting_room_id = ?"
        return self.cursor.execute(sql, (room_id,)).fetchall()

    def get_booking_by_user_id(self, user_id: int) -> tuple:
        """Get room by ID"""
        sql = "SELECT * FROM booking_bookinghistory WHERE booked_by_id = ?"
        return self.cursor.execute(sql, (user_id,)).fetchall()

    def get_room_by_id(self, room_id: int) -> tuple:
        """Get room by ID"""
        sql = "SELECT * FROM booking_meetingroom WHERE id = ?"
        return self.cursor.execute(sql, (room_id,)).fetchone()

    def add_new_room(self, room_name: str, capacity: int, is_active: int) -> None:
        """Add a new room to the database"""
        sql = "INSERT INTO booking_meetingroom (room_name, capacity, is_active) VALUES (?, ?, ?)"
        self.cursor.execute(sql, (room_name, capacity, int(is_active)))
        self.connection.commit()

    def call_report_generator(self, room_id) -> None:
        """Call the generate report function before deleting the booking room"""
        bookings_with_the_room_id = self.get_booking_by_room_id(room_id)
        user_ids = set(x[4] for x in bookings_with_the_room_id)
        user_booking_data = {}
        for user_id in user_ids:
            user_booking_data[user_id] = self.get_booking_by_user_id(user_id)
        all_users_affected = set()
        for i in bookings_with_the_room_id:
            all_users_affected.add(self.get_user_by_id(i[4]))

        print(f"user_booking_data {user_booking_data}")
        self.generate_report.generate_report( "DELETE",
                                             all_users_affected, bookings_with_the_room_id, user_booking_data)

    def delete_room_by_id(self, room_id):
        """Delete the booking with the room ID and the room as well"""
        self.call_report_generator(room_id)
        self.cursor.execute("DELETE FROM booking_bookinghistory WHERE meeting_room_id = ?", (room_id,))
        self.cursor.execute("DELETE FROM booking_meetingroom WHERE id = ?", (room_id,))
        self.connection.commit()

    def update_room(self, room_id: int, room_name: str, capacity: int, is_active: int) -> None:
        """Update a room in the database"""
        sql = "UPDATE booking_meetingroom SET room_name = ?, capacity = ?, is_active = ? WHERE id = ?"
        self.cursor.execute(sql,(room_name, capacity, int(is_active), room_id))
        self.connection.commit()
