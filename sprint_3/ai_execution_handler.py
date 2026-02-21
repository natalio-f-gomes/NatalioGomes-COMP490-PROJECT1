"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: ai_execution_handler.py
Purpose: This file handles the AI logic
"""

import json
import os
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic
from room_booking import RoomBooking


class FilterLogic:
    """
    Class responsible for loading the secrets, authenticate to api,
    call claude AI and filter by dictionary keys
    """

    def __init__(self):
        """
        Class Initializer
        """
        load_dotenv()
        self.room_instance = RoomBooking()
        self.room_instance.authenticate()
        self.all_my_bookings = self.room_instance.list_my_bookings()

    def filter_by_key(self, data: dict) -> list[dict]:
        """
        if the keys passed belongs to room call filter_room_by_key
        otherwise call filter_booking_by_key
        :param data: dict
        :return: list[dict]
        """
        for key, value in data.items():
            if key == "booking_id":
                self.filter_booking("id", int(value))
            elif key == "room_id":
                self.filter_room("id", int(value))
            elif key in {"room_name", "capacity"}:
                self.filter_room(key, value)
            elif key in {"start_time", "end_time"}:
                self.filter_booking(key, value)

        return self.all_my_bookings

    def filter_booking(self, key: str, value: str or int) -> None:
        """
        filters the bookings based on the data
        :param key:
        :param value:
        :return: None
        """
        self.all_my_bookings = [i for i in self.all_my_bookings
                                if str(i.get(key, '')).startswith(str(value))]

    def filter_room(self, key: str, value: str or int) -> None:
        """
       filters the rooms data based on the data
       :param key:
       :param value:
       :return: None
       """

        self.all_my_bookings = [i for i in self.all_my_bookings
                                if i['meeting_room'].get(key) == value]

    def get_content(self):
        """
        AI prompt
        :return: str
        """
        room_names = set(
            booking['meeting_room']['room_name'] for booking in self.all_my_bookings
        )
        return f""""You are a data extraction assistant. Given a user query,
            return ONLY a json format. No explanation.
            Make sure to convert the text number to numeral number every time
            ALL KEYS AND VALUES OF THE DICTIONARY MUST BE STRING in  double quotes
            Available room names: {room_names}
            IMPORTANT: Only use room names from this list. Match the user's input 
            to the closest room name from the list.
            Today's date is: {datetime.now().strftime('%Y-%m-%d')}
            Datetime format = YEAR-MONTH-DAY T HOUR:MIN:SEC
            Room data format example: dict 'id': 1, 'meeting_room': dict ('id': 1, 'room_name': 'Alpha', 'capacity': n), 
            'start_time': 'Datetime format', 'end_time': 'Datetime format'
            ATTENTION: Booking Only has booking_id, start_time and end_time
                       meeting_room: room_id, room_name, capacity
            if the user is looking for all booking or all rooms:
                ONLY return list_all_bookings
            Example:
            User: "when is my reservation for Room Alpha?"
            Output: dict key "room_name": dict value "Alpha", 
    
            User: "what rooms are booked on Feb 5?"  
            Output: dict "start_time": "2026-02-05",
            Return ONLY valid python dict. No other text.
            
            User: "Do I have a reservation in Room 1 today?" 
            Output:  dict key "room_name": dict value "Room 1" dict "start_time": 
                    "today's date in the format specified"
            return ONLY a json format. No explanation.
        """

    @staticmethod
    def clean_json_response(raw_message: str) -> str:
        """
        Gets the first {, rfind("}") gets the last }.
        :param raw_message:
        :return: str
        """
        start = raw_message.find("{")
        end = raw_message.rfind("}") + 1
        if start != -1 and end > 0:
            return raw_message[start:end]
        return raw_message

    def call_claude_ai(self, prompt: str) -> None:
        """
        Calls Claude AI and give it the prompt and filters the data
        :param prompt: str
        :return: None
        """
        print(f"prompt {prompt}")
        client = Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": f""" {self.get_content()}
                Prompt: {prompt}
                """}
            ]
        )
        raw_message = message.content[0].text
        clean_message = self.clean_json_response(raw_message)
        print(f"clean message {clean_message}")
        try:
            data = json.loads(clean_message)
            print(data)
            if "list_all_bookings" in data:
                print(self.all_my_bookings)
            print(f"DATA {data}")
            result = self.filter_by_key(data)
            print(f"RESULT: ")
            print(result)
            for room in result:
                print(f"Booking {room}")
        except json.decoder.JSONDecodeError as error:
            print(f"There was a problem with your prompt. {error}\nPlease try again.")
