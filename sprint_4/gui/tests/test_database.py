"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: test_database.py
Purpose: This file handles the Unit Testing
"""

import sqlite3
import pytest

from database_handler import DatabaseHandler

def create_meeting_room_table(connection):
    """create meeting room table"""
    connection.execute("""
                       CREATE TABLE booking_meetingroom
                       (
                           id        INTEGER PRIMARY KEY,
                           room_name TEXT,
                           capacity  INTEGER,
                           is_active BOOLEAN DEFAULT 1
                       )
                       """)
    connection.commit()

def create_booking_record_table(connection):
    """create booking record table"""
    connection.execute("""
                       CREATE TABLE booking_bookinghistory
                       (
                           id              INTEGER PRIMARY KEY,
                           start_time      TEXT,
                           end_time        TEXT,
                           no_of_persons   INTEGER,
                           booked_by_id    INTEGER,
                           meeting_room_id INTEGER
                       )
                       """)
    connection.commit()

def create_users_table(connection):
    """create users table"""
    connection.execute("""
                       CREATE TABLE member_customuser
                       (
                           id           INTEGER PRIMARY KEY,
                           password     TEXT,
                           last_login   TEXT,
                           is_active    BOOLEAN DEFAULT 1,
                           email        TEXT,
                           is_staff     BOOLEAN DEFAULT 0,
                           is_superuser BOOLEAN DEFAULT 0,
                           username     TEXT
                       )
                       """)
    connection.commit()

def create_rooms(db_instance):
    """create rooms for unit testing"""
    db_instance.connection.execute(
        "INSERT INTO booking_meetingroom (room_name, capacity, is_active) VALUES ('Room A', 10,1)")
    db_instance.connection.execute(
        "INSERT INTO booking_meetingroom (room_name, capacity, is_active) VALUES ('Room B', 20,1)")
    db_instance.connection.execute(
        "INSERT INTO booking_meetingroom (room_name, capacity, is_active) VALUES ('DMF 225', 15,1)")

def create_users(db_instance):
    """create temporary users for unit testing"""
    db_instance.connection.execute(
        "INSERT INTO member_customuser (password, last_login, email, is_active, is_staff, is_superuser, username) "
        "VALUES ('Password123@', '2026-03-08 14:45:33.216728','n1gomes@bridgew.edu',1,0,0, 'n1gomes')")

def create_record_history(db_instance):
    """Create  record history"""
    db_instance.connection.execute(
        "INSERT INTO booking_bookinghistory (start_time, end_time, no_of_persons, booked_by_id, meeting_room_id) VALUES"
        " ('2026-03-08 14:45:33.216728', '2026-03-08 15:00:33.216728',10,1,1)")

@pytest.fixture
def db_instance():
    """Set up the test database"""
    connection = sqlite3.connect(":memory:")
    database_instance = DatabaseHandler(connection)
    create_meeting_room_table(connection)
    create_booking_record_table(connection)
    create_users_table(connection)

    yield database_instance
    connection.close()

def test_get_all_rooms(db_instance):
    """Test Get all rooms in the database"""
    create_rooms(db_instance)
    all_rooms = db_instance.get_all_rooms()
    assert len(all_rooms) != 0

def test_get_user_by_id(db_instance):
    """Test Get User by id"""
    create_users(db_instance)
    user = db_instance.get_user_by_id(1)
    assert user is not None
    assert user[0] == 1

def test_get_booking_by_id(db_instance):
    """Test Get Booking by id"""

    create_record_history(db_instance)
    booking = db_instance.get_booking_by_id(1)
    assert booking[0][0] == 1

def test_get_booking_by_room_id(db_instance):
    """Test Get Booking by room id"""
    create_rooms(db_instance)
    create_record_history(db_instance)
    room = db_instance.get_room_by_id(1)
    booking = db_instance.get_booking_by_room_id(room[0])
    assert booking is not None
    assert booking[0][5] == room[0]

def test_get_booking_by_user_id(db_instance):
    """Test Get Booking by user id"""
    create_record_history(db_instance)
    booking = db_instance.get_booking_by_user_id(1)
    assert len(booking) == 1

def test_get_room_by_id(db_instance):
    """Test Get Room by id"""
    create_rooms(db_instance)
    room = db_instance.get_room_by_id(3)
    assert room[1] == "DMF 225"
    assert room[2] == 15
    assert room[3] == 1

def test_add_new_room(db_instance):
    """Test add a new room in the database"""
    db_instance.add_new_room("Testing Room", 4, 1)
    all_rooms = db_instance.get_all_rooms()
    assert all_rooms[-1][1] == "Testing Room"
    assert all_rooms[-1][2] == 4
    assert all_rooms[-1][3] == 1

def test_update_room(db_instance):
    """Test update a room in the database"""
    create_rooms(db_instance)
    room1 = db_instance.get_room_by_id(1)
    db_instance.update_room(1, "Board Room", 12, 1)
    room1_updated = db_instance.get_room_by_id(1)
    assert room1_updated[2] != room1[2]
    assert room1_updated[2] == 12

def test_delete_room_by_id(db_instance):
    """Test delete a room in the database"""
    create_rooms(db_instance)
    create_record_history(db_instance)
    create_users(db_instance)
    last_room_added = db_instance.get_all_rooms()[0]
    print(f"DEBUG: Last Room Added: {last_room_added}")
    db_instance.delete_room_by_id(last_room_added[0])
    assert len(db_instance.get_all_rooms()) == 2
