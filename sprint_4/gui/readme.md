# Author: Natalio Gomes
#### Class: COMP 490
#### Section: 003

## Project 1 – Sprint 4 GUI

### Prerequisites

- Git
- Python 3.11
- pyenv
- pip

## Setup Process

1. Clone the repository and navigate into the project folder

   ```bash
   git clone git@github.com:natalio-f-gomes/NatalioGomes-COMP490-PROJECT1.git
   cd sprint_4/gui
   ```

2. Check your current Python version

   ```bash
   python3 --version
   ```

3. Create and activate a virtual environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   
   ```

5. Upgrade Pip and Install Python dependencies

   ```bash
   pip3 install --upgrade pip
   pip3 install -r requirements.txt
   ```

6. Running the Application

```bash
python3 main.py # macOS
python main.py  # windows
```

Notes: Evrytime the user deletes a room, it writes the report located in **Report/report.csv**

8. Running Tests

```bash
python3 -m pytest tests/*
```


### Test Environment Setup

All tests use an **in-memory SQLite database** created using a pytest fixture:

* **Fixture:** `db_instance`
* **Purpose:**

  * Creates temporary tables:

    * `booking_meetingroom`
    * `booking_bookinghistory`
    * `member_customuser`
  * Ensures tests run in isolation.
  * Automatically cleans up the database after execution.

---

## Unit Tests

### 1. Retrieve All Meeting Rooms

* **Function Tested:** `get_all_rooms()`
* **Test Function:** `test_get_all_rooms`
* **Description:**
  Verifies that the system can retrieve all meeting rooms stored in the database.
* **Process:**

  * Insert sample rooms using `create_rooms`.
  * Call `get_all_rooms()`.
  * Confirm the returned list is not empty.

---

### 2. Retrieve User by ID

* **Function Tested:** `get_user_by_id(user_id)`
* **Test Function:** `test_get_user_by_id`
* **Description:**
  Ensures that a user can be retrieved from the database using their unique ID.
* **Process:**

  * Insert a test user using `create_users`.
  * Call `get_user_by_id(1)`.
  * Verify that a user record is returned and the ID matches.

---

### 3. Retrieve Booking by Booking ID

* **Function Tested:** `get_booking_by_id(booking_id)`
* **Test Function:** `test_get_booking_by_id`
* **Description:**
  Confirms that booking history records can be retrieved using a booking ID.
* **Process:**

  * Insert a booking record using `create_record_history`.
  * Call `get_booking_by_id(1)`.
  * Verify the returned booking has ID `1`.

---

### 4. Retrieve Booking by Room ID

* **Function Tested:** `get_booking_by_room_id(room_id)`
* **Test Function:** `test_get_booking_by_room_id`
* **Description:**
  Ensures bookings can be retrieved for a specific meeting room.
* **Process:**

  * Insert test rooms and a booking record.
  * Retrieve a room using `get_room_by_id`.
  * Call `get_booking_by_room_id(room_id)`.
  * Verify that the booking belongs to the correct room.

---

### 5. Retrieve Booking by User ID

* **Function Tested:** `get_booking_by_user_id(user_id)`
* **Test Function:** `test_get_booking_by_user_id`
* **Description:**
  Confirms that bookings associated with a specific user can be retrieved.
* **Process:**

  * Insert a booking record.
  * Call `get_booking_by_user_id(1)`.
  * Verify exactly one booking is returned.

---

### 6. Retrieve Room by ID

* **Function Tested:** `get_room_by_id(room_id)`
* **Test Function:** `test_get_room_by_id`
* **Description:**
  Validates that a meeting room can be retrieved using its ID.
* **Process:**

  * Insert sample rooms using `create_rooms`.
  * Retrieve room with ID `3`.
  * Confirm the room details match the expected values.

---

### 7. Add a New Room

* **Function Tested:** `add_new_room(room_name, capacity, is_active)`
* **Test Function:** `test_add_new_room`
* **Description:**
  Ensures a new meeting room can be added to the database.
* **Process:**

  * Call `add_new_room`.
  * Retrieve all rooms.
  * Verify the last inserted room matches the provided values.

---

### 8. Update an Existing Room

* **Function Tested:** `update_room(room_id, room_name, capacity, is_active)`
* **Test Function:** `test_update_room`
* **Description:**
  Validates that room information can be updated correctly.
* **Process:**
  * Insert sample rooms.
  * Update room with ID `1`.
  * Retrieve the updated room.
  * Confirm the capacity has changed to the new value.

---

### 9. Delete Room by ID

* **Function Tested:** `delete_room_by_id(room_id)`
* **Test Function:** `test_delete_room_by_id`
* **Description:**
  Removes the meeting room from the db
* **Process:**
  
  * Insert rooms, booking history, and users.
  * Delete a room using its ID.
  * Verify the number of rooms in the database decreases.

---


