"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: test_ai_execution_handler.py
Purpose: This file tests the methods of the ai_execution_handler.py file
"""

all_my_bookings = [
    {'id': 4, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-05T11:00:00Z',
     'end_time': '2026-02-05T12:15:00Z'},
    {'id': 91, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-09T15:24:00Z', 'end_time': '2026-02-09T16:24:00Z'},
    {'id': 92, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-09T16:03:00Z',
     'end_time': '2026-02-09T17:03:00Z'},
    {'id': 93, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-09T16:05:00Z', 'end_time': '2026-02-09T17:05:00Z'},
    {'id': 94, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24}, 'start_time': '2026-02-09T16:08:00Z',
     'end_time': '2026-02-09T17:08:00Z'},
    {'id': 153, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-10T19:07:00Z',
     'end_time': '2026-02-10T19:22:00Z'},
    {'id': 154, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-10T19:07:00Z',
     'end_time': '2026-02-10T19:22:00Z'},
    {'id': 155, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T11:00:00Z'},
    {'id': 156, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T10:15:00Z'},
    {'id': 157, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T10:15:00Z'},
    {'id': 158, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-10T10:00:00Z', 'end_time': '2026-02-10T10:15:00Z'},
    {'id': 159, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T10:15:00Z'},
    {'id': 160, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T10:15:00Z'},
    {'id': 161, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2026-02-10T10:00:00Z', 'end_time': '2026-02-10T10:15:00Z'},
    {'id': 162, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T10:15:00Z'},
    {'id': 163, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-10T10:00:00Z', 'end_time': '2026-02-10T10:15:00Z'},
    {'id': 165, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-10T20:26:00Z',
     'end_time': '2026-02-10T20:41:00Z'},
    {'id': 166, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-10T20:26:00Z',
     'end_time': '2026-02-10T20:41:00Z'},
    {'id': 269, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-11T18:00:00Z',
     'end_time': '2026-02-11T18:15:00Z'},
    {'id': 271, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-11T18:00:00Z',
     'end_time': '2026-02-11T18:15:00Z'},
    {'id': 274, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-11T19:08:00Z',
     'end_time': '2026-02-11T19:23:00Z'},
    {'id': 275, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-11T19:58:00Z',
     'end_time': '2026-02-11T20:13:00Z'},
    {'id': 276, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12}, 'start_time': '2026-02-11T20:07:00Z',
     'end_time': '2026-02-11T20:22:00Z'},
    {'id': 277, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-11T20:52:00Z',
     'end_time': '2026-02-11T21:07:00Z'},
    {'id': 278, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-11T21:36:00Z',
     'end_time': '2026-02-11T21:51:00Z'},
    {'id': 287, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T11:00:00Z',
     'end_time': '2026-02-12T11:15:00Z'},
    {'id': 288, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-12T11:00:00Z',
     'end_time': '2026-02-12T11:15:00Z'},
    {'id': 289, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-12T11:00:00Z',
     'end_time': '2026-02-12T11:15:00Z'},
    {'id': 291, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12}, 'start_time': '2026-02-12T11:00:00Z',
     'end_time': '2026-02-12T11:15:00Z'},
    {'id': 294, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T06:55:00Z',
     'end_time': '2026-02-12T07:10:00Z'},
    {'id': 295, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12}, 'start_time': '2026-02-12T07:00:00Z',
     'end_time': '2026-02-12T07:10:00Z'},
    {'id': 296, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-12T07:09:00Z',
     'end_time': '2026-02-12T07:19:00Z'},
    {'id': 297, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-12T07:13:00Z',
     'end_time': '2026-02-12T07:33:00Z'},
    {'id': 298, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12}, 'start_time': '2026-02-12T07:18:00Z',
     'end_time': '2026-02-12T07:34:00Z'},
    {'id': 299, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-12T07:19:00Z', 'end_time': '2026-02-12T07:32:00Z'},
    {'id': 300, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T07:19:00Z',
     'end_time': '2026-02-12T07:27:00Z'},
    {'id': 301, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-12T07:19:00Z',
     'end_time': '2026-02-12T07:27:00Z'},
    {'id': 302, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-12T07:19:00Z',
     'end_time': '2026-02-12T07:30:00Z'},
    {'id': 303, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24}, 'start_time': '2026-02-12T07:19:00Z',
     'end_time': '2026-02-12T07:33:00Z'},
    {'id': 304, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-12T07:19:00Z', 'end_time': '2026-02-12T07:30:00Z'},
    {'id': 305, 'meeting_room': {'id': 11, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-12T07:19:00Z',
     'end_time': '2026-02-12T07:36:00Z'},
    {'id': 306, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2026-02-12T07:19:00Z', 'end_time': '2026-02-12T07:25:00Z'},
    {'id': 307, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12}, 'start_time': '2026-02-12T07:19:00Z',
     'end_time': '2026-02-12T07:35:00Z'},
    {'id': 308, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T07:36:00Z',
     'end_time': '2026-02-12T07:51:00Z'},
    {'id': 309, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T08:04:00Z',
     'end_time': '2026-02-12T08:19:00Z'},
    {'id': 310, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T08:35:00Z',
     'end_time': '2026-02-12T08:50:00Z'},
    {'id': 313, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T09:09:00Z',
     'end_time': '2026-02-12T09:24:00Z'},
    {'id': 315, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T11:37:00Z',
     'end_time': '2026-02-12T11:52:00Z'},
    {'id': 316, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T11:55:00Z',
     'end_time': '2026-02-12T12:10:00Z'},
    {'id': 317, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-12T11:57:00Z',
     'end_time': '2026-02-12T12:12:00Z'},
    {'id': 318, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-12T12:09:00Z',
     'end_time': '2026-02-12T12:24:00Z'},
    {'id': 319, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T15:17:00Z',
     'end_time': '2026-02-12T15:32:00Z'},
    {'id': 320, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-12T15:20:00Z',
     'end_time': '2026-02-12T15:35:00Z'},
    {'id': 321, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T10:21:00Z',
     'end_time': '2026-02-12T10:36:00Z'},
    {'id': 323, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-12T11:34:00Z',
     'end_time': '2026-02-12T11:49:00Z'},
    {'id': 366, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24}, 'start_time': '2026-02-12T16:23:00Z',
     'end_time': '2026-02-12T16:38:00Z'},
    {'id': 367, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24}, 'start_time': '2026-02-12T18:19:00Z',
     'end_time': '2026-02-12T18:34:00Z'},
    {'id': 370, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24}, 'start_time': '2026-02-12T20:23:00Z',
     'end_time': '2026-02-12T20:38:00Z'},
    {'id': 371, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-12T20:24:00Z',
     'end_time': '2026-02-12T20:39:00Z'},
    {'id': 374, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T22:17:00Z',
     'end_time': '2026-02-12T22:32:00Z'},
    {'id': 384, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-12T11:00:00Z',
     'end_time': '2026-02-12T11:15:00Z'},
    {'id': 388, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T22:40:00Z',
     'end_time': '2026-02-12T22:55:00Z'},
    {'id': 392, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2003-09-29T11:00:00Z',
     'end_time': '2003-09-29T11:15:00Z'},
    {'id': 395, 'meeting_room': {'id': 11, 'room_name': '9', 'capacity': 20}, 'start_time': '2020-09-09T11:00:00Z',
     'end_time': '2020-09-09T11:15:00Z'},
    {'id': 399, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T18:45:00Z',
     'end_time': '2026-02-12T19:00:00Z'},
    {'id': 413, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T19:16:00Z',
     'end_time': '2026-02-12T19:31:00Z'},
    {'id': 417, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-12T19:50:00Z',
     'end_time': '2026-02-12T20:05:00Z'},
    {'id': 419, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-12T18:57:00Z',
     'end_time': '2026-02-12T19:12:00Z'},
    {'id': 426, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-12T19:05:00Z',
     'end_time': '2026-02-12T19:20:00Z'},
    {'id': 485, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12}, 'start_time': '2026-02-12T21:03:00Z',
     'end_time': '2026-02-12T21:18:00Z'},
    {'id': 497, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12}, 'start_time': '2026-02-12T21:25:00Z',
     'end_time': '2026-02-12T21:40:00Z'},
    {'id': 501, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-12T21:14:00Z',
     'end_time': '2026-02-12T21:29:00Z'},
    {'id': 502, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12}, 'start_time': '2026-02-12T21:19:00Z',
     'end_time': '2026-02-12T21:34:00Z'},
    {'id': 558, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-13T03:35:00Z',
     'end_time': '2026-02-13T03:50:00Z'},
    {'id': 561, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-12T22:41:00Z', 'end_time': '2026-02-12T22:56:00Z'},
    {'id': 588, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12}, 'start_time': '2026-02-13T01:27:00Z',
     'end_time': '2026-02-13T01:42:00Z'},
    {'id': 686, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-13T18:57:00Z',
     'end_time': '2026-02-13T19:12:00Z'},
    {'id': 690, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-13T19:18:00Z',
     'end_time': '2026-02-13T19:33:00Z'},
    {'id': 691, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-13T19:33:00Z',
     'end_time': '2026-02-13T19:48:00Z'},
    {'id': 781, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-14T00:20:00Z',
     'end_time': '2026-02-14T00:35:00Z'},
    {'id': 802, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-14T06:09:00Z',
     'end_time': '2026-02-14T06:24:00Z'},
    {'id': 1003, 'meeting_room': {'id': 11, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T10:15:00Z'},
    {'id': 1005, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-10T10:00:00Z',
     'end_time': '2026-02-10T10:15:00Z'},
    {'id': 1006, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-15T18:26:00Z',
     'end_time': '2026-02-15T18:41:00Z'},
    {'id': 1007, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-15T13:39:00Z',
     'end_time': '2026-02-15T13:54:00Z'},
    {'id': 1009, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-15T13:42:00Z',
     'end_time': '2026-02-15T13:57:00Z'},
    {'id': 1011, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-15T19:43:00Z',
     'end_time': '2026-02-15T19:58:00Z'},
    {'id': 1013, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-15T19:45:00Z',
     'end_time': '2026-02-15T20:00:00Z'},
    {'id': 1014, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-15T13:50:00Z',
     'end_time': '2026-02-15T14:05:00Z'},
    {'id': 1015, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12},
     'start_time': '2026-02-15T14:48:00Z', 'end_time': '2026-02-15T15:03:00Z'},
    {'id': 1017, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-15T19:54:00Z',
     'end_time': '2026-02-15T20:09:00Z'},
    {'id': 1018, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-15T19:54:00Z', 'end_time': '2026-02-15T20:09:00Z'},
    {'id': 1019, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12},
     'start_time': '2026-02-15T20:11:00Z', 'end_time': '2026-02-15T20:26:00Z'},
    {'id': 1020, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-15T20:26:00Z', 'end_time': '2026-02-15T20:41:00Z'},
    {'id': 1021, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-15T20:41:00Z', 'end_time': '2026-02-15T20:56:00Z'},
    {'id': 1022, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-15T20:56:00Z',
     'end_time': '2026-02-15T21:11:00Z'},
    {'id': 1023, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-15T21:11:00Z',
     'end_time': '2026-02-15T21:26:00Z'},
    {'id': 1024, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12},
     'start_time': '2026-02-15T21:26:00Z', 'end_time': '2026-02-15T21:41:00Z'},
    {'id': 1025, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-15T21:41:00Z', 'end_time': '2026-02-15T21:56:00Z'},
    {'id': 1027, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-15T19:00:00Z',
     'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1029, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-15T19:00:00Z', 'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1030, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12},
     'start_time': '2026-02-15T19:12:00Z', 'end_time': '2026-02-15T19:27:00Z'},
    {'id': 1031, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-15T19:15:00Z', 'end_time': '2026-02-15T19:30:00Z'},
    {'id': 1032, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-15T19:00:00Z', 'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1035, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-15T19:00:00Z',
     'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1036, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12},
     'start_time': '2026-02-15T19:00:00Z', 'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1037, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '3000-01-01T14:00:00Z',
     'end_time': '3000-01-01T14:15:00Z'},
    {'id': 1039, 'meeting_room': {'id': 11, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-15T19:00:00Z',
     'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1040, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2026-02-15T19:00:00Z', 'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1041, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-15T19:30:00Z', 'end_time': '2026-02-15T19:45:00Z'},
    {'id': 1042, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-15T19:00:00Z',
     'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1044, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2026-02-15T19:00:00Z',
     'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1045, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24},
     'start_time': '2026-02-15T19:35:00Z', 'end_time': '2026-02-15T19:50:00Z'},
    {'id': 1046, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24},
     'start_time': '2026-02-15T19:00:00Z', 'end_time': '2026-02-15T19:15:00Z'},
    {'id': 1048, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2026-02-15T19:37:00Z', 'end_time': '2026-02-15T19:52:00Z'},
    {'id': 1052, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-15T14:57:00Z',
     'end_time': '2026-02-15T15:12:00Z'},
    {'id': 1053, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-15T14:57:00Z',
     'end_time': '2026-02-15T15:12:00Z'},
    {'id': 1055, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12},
     'start_time': '2026-02-15T15:03:00Z', 'end_time': '2026-02-15T15:18:00Z'},
    {'id': 1062, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-15T20:44:00Z',
     'end_time': '2026-02-15T20:59:00Z'},
    {'id': 1065, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-15T16:08:00Z',
     'end_time': '2026-02-15T16:23:00Z'},
    {'id': 1072, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24},
     'start_time': '2026-02-15T16:16:00Z', 'end_time': '2026-02-15T16:31:00Z'},
    {'id': 1075, 'meeting_room': {'id': 11, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-15T16:21:00Z',
     'end_time': '2026-02-15T16:36:00Z'},
    {'id': 1084, 'meeting_room': {'id': 11, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-15T16:55:00Z',
     'end_time': '2026-02-15T17:10:00Z'},
    {'id': 1100, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24},
     'start_time': '2026-02-15T17:19:00Z', 'end_time': '2026-02-15T17:39:00Z'},
    {'id': 1105, 'meeting_room': {'id': 11, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-15T17:37:00Z',
     'end_time': '2026-02-15T17:57:00Z'},
    {'id': 1106, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12},
     'start_time': '2026-02-15T22:38:00Z', 'end_time': '2026-02-15T22:58:00Z'},
    {'id': 1109, 'meeting_room': {'id': 9, 'room_name': 'Welcome Center 210', 'capacity': 20},
     'start_time': '2026-02-15T17:40:00Z', 'end_time': '2026-02-15T18:00:00Z'},
    {'id': 1116, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-15T22:43:00Z',
     'end_time': '2026-02-15T23:03:00Z'},
    {'id': 1121, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12},
     'start_time': '2026-02-15T17:49:00Z', 'end_time': '2026-02-15T18:09:00Z'},
    {'id': 1122, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24},
     'start_time': '2026-02-15T22:49:00Z', 'end_time': '2026-02-15T23:09:00Z'},
    {'id': 1125, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2026-02-15T22:50:00Z', 'end_time': '2026-02-15T23:10:00Z'},
    {'id': 1145, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2090-01-01T14:00:00Z',
     'end_time': '2090-01-01T14:15:00Z'},
    {'id': 1193, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2026-02-15T20:49:00Z', 'end_time': '2026-02-15T21:04:00Z'},
    {'id': 1199, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12},
     'start_time': '2026-02-15T21:08:00Z', 'end_time': '2026-02-15T21:23:00Z'},
    {'id': 1200, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-15T21:12:00Z', 'end_time': '2026-02-15T21:27:00Z'},
    {'id': 1215, 'meeting_room': {'id': 2, 'room_name': 'Room B', 'capacity': 10}, 'start_time': '2026-02-15T23:39:00Z',
     'end_time': '2026-02-15T23:54:00Z'},
    {'id': 1229, 'meeting_room': {'id': 6, 'room_name': 'DMF 363', 'capacity': 24},
     'start_time': '2026-02-16T00:23:00Z', 'end_time': '2026-02-16T00:38:00Z'},
    {'id': 1230, 'meeting_room': {'id': 10, 'room_name': '9', 'capacity': 20}, 'start_time': '2026-02-16T00:25:00Z',
     'end_time': '2026-02-16T00:40:00Z'},
    {'id': 1235, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-16T06:29:00Z',
     'end_time': '2026-02-16T06:44:00Z'},
    {'id': 1258, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2026-02-16T18:29:00Z', 'end_time': '2026-02-16T18:49:00Z'},
    {'id': 1311, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2026-02-18T17:47:00Z', 'end_time': '2026-02-18T18:02:00Z'},
    {'id': 1328, 'meeting_room': {'id': 5, 'room_name': 'DMF 471', 'capacity': 12},
     'start_time': '2026-02-19T13:45:00Z', 'end_time': '2026-02-19T14:00:00Z'},
    {'id': 1340, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2026-02-20T03:26:00Z',
     'end_time': '2026-02-20T03:46:00Z'},
    {'id': 1342, 'meeting_room': {'id': 7, 'room_name': 'DMF Small Office', 'capacity': 4},
     'start_time': '2032-01-03T19:45:00Z', 'end_time': '2032-01-03T20:00:00Z'},
    {'id': 1343, 'meeting_room': {'id': 4, 'room_name': 'DMF 473', 'capacity': 12},
     'start_time': '2030-07-16T02:15:00Z', 'end_time': '2030-07-16T02:30:00Z'},
    {'id': 1344, 'meeting_room': {'id': 8, 'room_name': 'Welcome Center 206', 'capacity': 15},
     'start_time': '2030-11-14T17:30:00Z', 'end_time': '2030-11-14T17:45:00Z'},
    {'id': 1345, 'meeting_room': {'id': 1, 'room_name': 'Room A', 'capacity': 4}, 'start_time': '2033-01-04T18:30:00Z',
     'end_time': '2033-01-04T18:45:00Z'},
    {'id': 1346, 'meeting_room': {'id': 3, 'room_name': 'Room C', 'capacity': 3}, 'start_time': '2033-07-28T05:45:00Z',
     'end_time': '2033-07-28T06:00:00Z'}]


def filter_booking_by_key(all_my_bookings, key: str, value: str or int) -> None:
    """
    filters the bookings based on the data
    :param key:
    :param value:
    :return: None
    """

    all_my_bookings = [i for i in all_my_bookings
                       if str(i.get(key, '')).startswith(str(value))]
    return all_my_bookings


{'room_name': 'DMF 473'}


def filter_room(all_my_bookings, key: str, value: str or int) -> None:
    """
    filters the rooms data based on the data
    :param key:
    :param value:
    :return: None
    """

    all_my_bookings = [i for i in all_my_bookings
                       if i['meeting_room'].get(key) == value]
    return all_my_bookings


r5 = filter_room(all_my_bookings, 'room_name', 'DMF 473')
r6 = filter_room(all_my_bookings, 'room_name', 'DMF A')
rooms = set()
for i in all_my_bookings:
    rooms.add(i["meeting_room"]["room_name"])
for room in rooms:
    print(f"{room} reservation {filter_room(all_my_bookings, "room_name", room)}")
# assert that these rooms do in fact exists and have reservations


for i in r5:
    pass
    # print(i)

r1 = filter_booking_by_key(all_my_bookings, 'id', '317')
r2 = filter_booking_by_key(all_my_bookings, 'start_time', '2026-02-09')
r3 = filter_booking_by_key(all_my_bookings, 'end_time', '2026-02-09T17:03')
r4 = filter_booking_by_key(all_my_bookings, 'end_time', '2026-02-09T17:03:15')
# assert that these bookings do in fact exists and have reservations


"""
DMF 473
DMF Small Office
Welcome Center 206
Room A
DMF 363
Room B
Welcome Center 210
DMF 471
Room C
9
"""
