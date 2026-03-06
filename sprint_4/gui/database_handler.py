"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: database_handler.py
Purpose: This file handles Database CRUD functionalities
"""

import sqlite3

class DatabaseHandler:
    """
    Database Handler Class with all necessary methods for sprint_4
    """
    def __init__(self):
        """Initialize the constructor by loading the db"""
        self.connection = sqlite3.connect('db.sqlite3')
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

    def get_all_rooms(self) -> list[tuple]:
        """Get all rooms"""
        command = """SELECT * FROM booking_meetingroom"""
        return self.cursor.execute(command).fetchall()

    def get_room_by_id(self, room_id: int) -> tuple:
        """Get room by ID"""
        sql = "SELECT * FROM booking_meetingroom WHERE id = ?"
        return self.cursor.execute(sql, (room_id,)).fetchone()

    def add_new_room(self, room_name: str, capacity: int, is_active: int) -> None:
        """Add a new room to the database"""
        sql = "INSERT INTO booking_meetingroom (room_name, capacity, is_active) VALUES (?, ?, ?)"
        self.cursor.execute(sql, (room_name, capacity, int(is_active)))
        self.connection.commit()

    def delete_room_by_id(self, room_id):
        self.cursor.execute("DELETE FROM booking_bookinghistory WHERE meeting_room_id = ?", (room_id,))
        self.cursor.execute("DELETE FROM booking_meetingroom WHERE id = ?", (room_id,))
        self.connection.commit()

    def update_room(self, room_id: int, room_name: str, capacity: int, is_active: int) -> None:
        """Update a room in the database"""
        sql = "UPDATE booking_meetingroom SET room_name = ?, capacity = ?, is_active = ? WHERE id = ?"
        self.cursor.execute(sql,(room_name, capacity, int(is_active), room_id))
        self.connection.commit()
