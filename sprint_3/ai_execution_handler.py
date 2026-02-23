"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: ai_execution_handler.py
Purpose: This file handles the AI logic
"""

import json
import os
from dotenv import load_dotenv
from anthropic import Anthropic
from room_booking import RoomBooking
from prompt import get_prompt


class FilterLogic:
    """
    Class responsible for loading the secrets, authenticate to api,
    call claude AI and filter by dictionary keys
    """

    def __init__(self):
        """
        Class Initializer that loads the secrets
        and authenticate to api
        """
        load_dotenv(override=False)
        self.room_instance = RoomBooking()
        self.room_instance.authenticate()
        self.all_my_bookings = self.room_instance.list_my_bookings()

    def filter_by_ai_data(self, data: dict) -> list[dict]:
        """
        if the keys passed belongs to room call filter_room
        otherwise call filter_booking
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

    def filter_booking(self, key: str, value: object) -> None:
        """
        filters the bookings based on the data
        :param key:
        :param value:
        :return: None
        """
        self.all_my_bookings = [i for i in self.all_my_bookings
                                if str(i.get(key, '')).startswith(str(value))]

    def filter_room(self, key: str, value: object) -> None:
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
        return get_prompt(room_names)

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

    def call_claude_ai(self, prompt: str) -> dict:
        """
        Calls Claude AI and give it the prompt and filters the data
        :param prompt: str
        :return: None
        """
        print(f"Prompt {prompt}")
        client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
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
        print(f"raw message: {raw_message}")
        clean_message = self.clean_json_response(raw_message)
        print(f"clean message {clean_message}")
        data = json.loads(clean_message)
        return data

    def call_ai_model(self, prompt: str):
        """
        takes in the prompt and calls the LLM that we are currently using
        """
        try:
            data = self.call_claude_ai(prompt)
            print(f"DATA returned: {data}")
            if data == {}:
                print("There was no result that matches your prompt. Please try again")
                return
            if "list_all_bookings" in data:
                print("RESULT: ")
                for i in self.all_my_bookings:
                    print(i)
                return
            result = self.filter_by_ai_data(data)
            print("RESULT: ")
            for room in result:
                print(f"Booking {room}")
        except json.decoder.JSONDecodeError as error:
            print(f"There was a problem with your prompt. {error}\nPlease try again.")
            raise
