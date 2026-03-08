import os
import pytest

from database_handler import DatabaseHandler

@pytest.fixture
def db_instance():
    """Set up the test database"""
    database_instance = DatabaseHandler()
    database_instance.database_path = "tests/db.sqlite3"
    return database_instance

def test_get_all_rooms(db_instance):
    """Test Get all rooms in the database"""
    all_rooms = db_instance.get_all_rooms()
    assert len(all_rooms) != 0

def test_get_user_by_id(db_instance):
    """Test Get User by id"""
    user = db_instance.get_user_by_id(7)
    assert user is not None
    assert user[0] == 7

def test_get_booking_by_id(db_instance):
    """Test Get Booking by id"""
    booking = db_instance.get_booking_by_id(168)
    booking_2 = db_instance.get_booking_by_id(0)
    assert booking_2 == []
    assert booking[0][0] == 168

def test_get_booking_by_room_id(db_instance):
    """Test Get Booking by room id"""
    room = db_instance.get_room_by_id(5)
    booking = db_instance.get_booking_by_room_id(room[0])
    assert booking is not None
    assert booking[0][5] == room[0]

def test_get_booking_by_user_id(db_instance):
    """Test Get Booking by user id"""
    booking = db_instance.get_booking_by_user_id(7)
    assert len(booking) == 228

def test_get_room_by_id(db_instance):
    """Test Get Room by id"""
    room = db_instance.get_room_by_id(4)
    assert room[1] == "DMF 473"
    assert room[2] == 12

def test_add_new_room(db_instance):
    """Test add a new room in the database"""
    db_instance.add_new_room("Testing Room", 4, 1)
    all_rooms = db_instance.get_all_rooms()
    assert all_rooms[-1][1] == "Testing Room"
    assert all_rooms[-1][2] == 4
    assert all_rooms[-1][3] == 1

def test_update_room(db_instance):
    """Test update a room in the database"""
    room1 = db_instance.get_room_by_id(1)
    db_instance.update_room(1, "Board Room", 12, 1)
    room1_updated = db_instance.get_room_by_id(1)
    assert room1_updated[2] != room1[2]
    assert room1_updated[2] == "12"

def test_delete_room_by_id(db_instance):
    """Test delete a room in the database"""
    last_room_added = db_instance.get_all_rooms()[-1]
    db_instance.delete_room_by_id(last_room_added[0])
    assert last_room_added is None
