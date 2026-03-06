import sqlite3


class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def get_all_rooms(self):
        command = """SELECT * FROM booking_meetingroom"""
        return self.cursor.execute(command).fetchall()

    def get_room_by_id(self, room_id):
        command = "SELECT * FROM booking_meetingroom WHERE id = ?"
        return self.cursor.execute(command, (room_id,)).fetchone()

    def add_new_room(self, room_name, capacity, is_active):
        command = "INSERT INTO booking_meetingroom (room_name, capacity, is_active) VALUES (?, ?, ?)"
        self.cursor.execute(command, (room_name, capacity, int(is_active)))
        self.connection.commit()

    def delete_room_by_id(self, room_id):
        self.cursor.execute("DELETE FROM booking_meetingroom WHERE id = ?", (room_id,))
        self.connection.commit()

    def update_room(self, room_id, room_name, capacity, is_active):
        self.cursor.execute("UPDATE booking_meetingroom SET room_name = ?, capacity = ?, is_active = ? WHERE id = ?",
                              (room_name, capacity, int(is_active), room_id))
        self.connection.commit()