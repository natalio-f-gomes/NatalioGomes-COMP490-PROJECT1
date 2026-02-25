"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: ai_execution_handler.py
Purpose: This file handles the AI logic
"""

import json
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
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
        return raw_message.strip().removeprefix("```json").removesuffix("```").strip()

    def call_claude_ai(self, prompt: str) -> dict or None:
        """
        Calls Claude AI and give it the prompt and filters the data
        The ChatAnthropic reads ANTHROPIC_API_KEY from os.environ by default
        :param prompt: str
        :return: None
        """
        llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")
        messages = [
            SystemMessage(content=self.get_content()),
            HumanMessage(content=prompt),
        ]
        response = llm.invoke(messages)
        print(f"DEBUG: Response Returned {response}")
        raw = response.content
        print(f"DEBUG: Raw Message Returned {raw}")
        cleaned = self.clean_json_response(raw)
        print(f"DEBUG: Cleaned Returned {cleaned}")
        try:
            data = json.loads(cleaned)
            print(f"DEBUG: Data Json {data}")
            return data
        except json.JSONDecodeError as e:
            print(f"There was a problem with your prompt. {e}\nPlease try again.")
            return None

    def display_data_in_terminal(self, data: dict) -> None:
        """
        Responsible for getting the data and displaying it in the terminal
        """
        if data == {}:
            print("There was no result that matches your prompt. Please try again")
            return
        if "list_all_bookings" in data:
            print("RESULT: ")
            print(f"{'=' * 200}")
            for i in self.all_my_bookings:
                print(i)
            print(f"{'=' * 200}")
            return
        result = self.filter_by_ai_data(data)
        print(f"There was {len(result)} result(s):")
        print(f"{'=' * 200}")
        for room in result:
            print(f"Booking {room}")
        print(f"{'=' * 200}")

    def call_ai_agentic_builder(self, prompt: str):
        """
        takes in the prompt and calls the LLM that we are currently using
        """
        data = self.call_claude_ai(prompt)
        print(f"DATA returned: {data}")
        self.display_data_in_terminal(data)
