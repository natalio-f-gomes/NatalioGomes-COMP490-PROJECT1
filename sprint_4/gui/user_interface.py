"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: user_interface.py
Purpose: This file handles the AI logic
"""
import os
import tkinter
from PIL import Image
import customtkinter
from database_handler import DatabaseHandler

class UserInterface:
    """User Interface class"""
    width = 1000
    height = 700
    def __init__(self):
        """User Interface constructor method"""
        self.room_to_be_updated = None
        self.update_room_frame = None
        self.database_instance = DatabaseHandler()
        self.all_rooms = self.database_instance.get_all_rooms()
        self.new_room_frame = None
        self.welcome_frame = None
        self.main_frame = None
        self.username_entry = None
        self.valid_room_name = None

        self.app = customtkinter.CTk()
        self.app.geometry(f"{self.width}x{self.height}")
        self.app.title("Room Booking Application")
        self.app.resizable(width=False, height=False)
        self.username = None

    def load_background_image(self) -> None:
        """Load the background image"""
        current_path = os.path.dirname(__file__)
        image = customtkinter.CTkImage(Image.open(current_path + "/images/nature.png"),
                                       size=(self.width,self.height))
        background_image = customtkinter.CTkLabel(self.app,image=image)
        background_image.grid(row=0,column=0)

    def load_main_frame(self) -> None:
        """Load the main frame along with the table of data"""
        self.main_frame = customtkinter.CTkFrame(master=self.app)
        self.main_frame.grid_columnconfigure(0, weight=1)
        welcome_label = customtkinter.CTkLabel(self.main_frame,
                                        text = f"Welcome {self.username_entry.get()}",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome_label.grid(row=0, column=0, padx=30, pady=(5, 5))
        intro_label =customtkinter.CTkLabel(self.main_frame, text = "List of All rooms",
                                             font=customtkinter.CTkFont(size=20))
        intro_label.grid(row=1, column=0, padx=30, pady=(5, 5))
        add_new_room_button = customtkinter.CTkButton(self.main_frame, text="Add a new Room",
                        command = self.add_new_room_navigator ,width=200)
        add_new_room_button.grid(row=2, column=0, padx=30, pady=(15, 15))

        table_frame = customtkinter.CTkScrollableFrame(master=self.main_frame, width=800, height=400)
        table_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        for i, col in enumerate(["ID", "Name", "Capacity", "Is Active?", "Options"]):
            table_frame.grid_columnconfigure(i, weight=1)
            header = customtkinter.CTkLabel(table_frame, text=col,
                                            font=customtkinter.CTkFont(weight="bold"))
            header.grid(row=0, column=i, padx=5, pady=5)
        self.fill_table( table_frame)

    def fill_table(self, table_frame: object) -> None:
        """
        Get the table frame and fill it with all rooms
        :param table_frame: customtkinter.CTkLabel
        :return: None
        """
        # clear all rows except header
        for widget in table_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()

        for i, row in enumerate(self.all_rooms, start=1):
            room_id, name, capacity, is_active ,= row
            is_active_display = "True" if is_active == 1 else "False"

            customtkinter.CTkLabel(table_frame, text=room_id).grid(row=i, column=0, padx=5, pady=5)
            customtkinter.CTkLabel(table_frame, text=name).grid(row=i, column=1, padx=5, pady=5)
            customtkinter.CTkLabel(table_frame, text=capacity).grid(row=i, column=2, padx=5, pady=5)
            customtkinter.CTkLabel(table_frame, text=is_active_display).grid(row=i, column=3, padx=5, pady=5)
            customtkinter.CTkLabel(table_frame, text="Options").grid(row=i, column=4, padx=5, pady=5)


            btn_frame = customtkinter.CTkFrame(table_frame, fg_color="transparent")
            btn_frame.grid(row=i, column=4, padx=5, pady=5)

            customtkinter.CTkButton(btn_frame, text="Update", width=70,
                                    command=lambda r=row: self.navigate_to_update_room(r)).pack(side="left", padx=2)
            customtkinter.CTkButton(btn_frame, text="Delete", width=70, fg_color="red", hover_color="#8b0000",
                                    command=lambda r=row: self.confirm_delete(r)).pack(side="left", padx=2)

    def confirm_room_deletion(self, message: str, on_confirm: object) -> None:
        """Ensuring the users wants to delete the room"""
        popup = customtkinter.CTkToplevel(self.app)
        popup.title("Confirm")
        popup.geometry("300x150")
        popup.resizable(False, False)

        label = customtkinter.CTkLabel(popup, text=message,
                                       font=customtkinter.CTkFont(size=14))
        label.pack(pady=20)
        btn_frame = customtkinter.CTkFrame(popup, fg_color="transparent")
        btn_frame.pack(pady=10)
        customtkinter.CTkButton(btn_frame, text="Confirm", width=100,
                                command=lambda: [on_confirm(), popup.destroy()]).pack(side="left", padx=10)
        customtkinter.CTkButton(btn_frame, text="Cancel", width=100, fg_color="grey",
                                command=popup.destroy).pack(side="left", padx=10)

    def confirm_delete(self, room: tuple) -> None:
        """
        If the user decides to proceed with deletion, call the delete_room funciton
        :param room:
        :return: None
        """
        self.confirm_room_deletion(
            f"You would Like to Delete Room {room[0]}?",
            on_confirm = lambda: self.delete_room(room)
        )

    def delete_room(self, room: tuple) -> None:
        """
        Delete the room by id
        :param room: tuple
        :return: None
        """
        print(f"Delete: {room}")
        self.database_instance.delete_room_by_id(room[0])
        self.all_rooms = self.database_instance.get_all_rooms()
        self.main_frame.grid_forget()
        self.load_main_frame()
        self.main_frame.grid(row=0, column=0, sticky="ns")

    def navigate_to_update_room(self, room: tuple) -> None:
        """
        Navigate to the room by id frame
        :param room: tuple
        :return: None
        """
        print(f"Update: {room}")
        self.room_to_be_updated = room
        self.main_frame.grid_forget()
        self.load_update_room_frame()
        self.update_room_frame.grid(row=0, column=0, sticky="nsew")

    def sanitize_data(self, room_name: str, capacity: int, is_active:bool) -> tuple or None:
        """
        Sanitize the data of the room
        :param room_name: str
        :param capacity: int
        :param is_active: boolean
        :return: tuple or None
        """
        symbols = """`~!@#$%^&*()_+{}[];:'",<.>/?|\\"""
        if room_name == "" or capacity == "":
            return None
        for letter in room_name:
            if letter in symbols:
                self.valid_room_name = False
                return "Invalid room name"
        try:
            capacity = int(capacity)
        except ValueError:
            self.valid_room_name = False
            return "Invalid capacity"
        if not isinstance(is_active, bool):
            self.valid_room_name = False
            return "Invalid is_active"
        self.valid_room_name = True
        return room_name, capacity, is_active

    def reload_main_frame(self, old_frame: tkinter.Grid) -> None:
        """
        Reload the main frame
        :param old_frame:
        :return:
        """
        self.all_rooms = self.database_instance.get_all_rooms()
        old_frame.grid_forget()
        self.main_frame.grid_forget()
        self.load_main_frame()
        self.main_frame.grid(row=0, column=0, sticky="ns")

    def add_new_room(self, room_name: str, room_capacity: int, is_room_active: bool)-> None:
        """
        Add a new room method
        :param room_name: str
        :param room_capacity: int
        :param is_room_active: bool
        :return: None
        """
        try:
            room_name, capacity, is_active = self.sanitize_data(room_name, room_capacity, bool(is_room_active))
            print(room_name, capacity, is_active)
            self.database_instance.add_new_room(room_name, capacity, is_room_active)
            self.reload_main_frame(self.new_room_frame)

        except ValueError:
            message = ("Not all fields were properly filled.\n"
                       "Room Name cannot be empty and the capacity must be a valid Integer")
            self.show_warning(message)

    def show_warning(self, message: str) -> None:
        """
        Display a warning message to the user
        :param message: str
        :return: None
        """
        popup = customtkinter.CTkToplevel(self.app)
        popup.title("Warning")
        popup.geometry("500x150")
        popup.resizable(False, False)

        label = customtkinter.CTkLabel(popup, text=message, font=customtkinter.CTkFont(size=14))
        label.pack(pady=30)

        ok_button = customtkinter.CTkButton(popup, text="OK", command=popup.destroy, width=100)
        ok_button.pack()

    def update_room(self, room_id:int, new_name:str, new_capacity:int, is_room_active:bool) -> None:
        """
        Sanitize the data of the room and then attempt to update it
        Update a room
        :param room_id: int
        :param new_name: str
        :param new_capacity: str
        :param is_room_active: bool
        :return: None
        """
        try:
            room_name, capacity, is_active = self.sanitize_data(new_name, new_capacity, bool(is_room_active))
            print(room_name, capacity, is_active)
            self.database_instance.update_room(room_id, room_name, capacity, is_room_active)
            self.reload_main_frame(self.update_room_frame)
        except (TypeError, ValueError):
            message = ("Not all fields were properly filled.\n"
                       "Room Name cannot be empty and the capacity must be a valid Integer")
            self.show_warning(message)

    def add_new_room_navigator(self) -> None:
        """
        Send the user to the page where you add a new room
        :return: None
        """
        self.main_frame.grid_forget()
        self.load_add_room_frame()
        self.new_room_frame.grid(row=0, column=0, sticky="nsew")

    def load_add_room_frame(self) -> None:
        """
        Add new room frame
        :return:
        """
        self.new_room_frame = customtkinter.CTkFrame(master=self.app)
        welcome_label = customtkinter.CTkLabel(self.new_room_frame, text="Adding a new room",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome_label.grid(row=0, column=1, padx=30, pady=(100, 15))

        room_name_label = customtkinter.CTkLabel(self.new_room_frame, text="Room Name",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        room_name_label.grid(row=1, column=0, padx=30, pady=(10, 15))
        room_name_entry = customtkinter.CTkEntry(self.new_room_frame, width=200,
                                                 placeholder_text="Room Name")
        room_name_entry.grid(row=1, column=2,  padx=30, pady=(10, 15))

        room_capacity_lbl = customtkinter.CTkLabel(self.new_room_frame, text="Room Capacity",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        room_capacity_lbl.grid(row=2, column=0, padx=30, pady=(10, 15))
        room_capacity_entry = customtkinter.CTkEntry(self.new_room_frame, width=200,
                                                     placeholder_text="Room Capacity")
        room_capacity_entry.grid(row=2, column=2, padx=30, pady=(10, 15))

        is_room_active_label = customtkinter.CTkLabel(self.new_room_frame, text="Is Room Active ?",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
        is_room_active_label.grid(row=3, column=0, padx=30, pady=(10, 15))
        is_room_active_checkbox = customtkinter.CTkCheckBox(self.new_room_frame, text="")
        is_room_active_checkbox.grid(row=3, column=2,  padx=30, pady=(10, 15))

        add_room_button = customtkinter.CTkButton(self.new_room_frame, command =
        lambda: self.add_new_room(room_name_entry.get(), room_capacity_entry.get(),
                                  is_room_active_checkbox.get()), text="Add Room" ,width=200)
        add_room_button.grid(row=4, column=1, padx=30, pady=(15, 15))

    def load_update_room_frame(self) -> None:
        """update room frame"""
        self.update_room_frame = customtkinter.CTkFrame(master=self.app)
        welcome_label = customtkinter.CTkLabel(self.update_room_frame,
                text=f"Updating room {self.room_to_be_updated[0]}",
                font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome_label.grid(row=0, column=1, padx=30, pady=(100, 15))

        room_name_label = customtkinter.CTkLabel(self.update_room_frame, text="Room Name",
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        room_name_label.grid(row=1, column=0, padx=30, pady=(10, 15))
        room_name_entry = customtkinter.CTkEntry(self.update_room_frame, width=200,
                                            placeholder_text=f"{self.room_to_be_updated[1]}")
        room_name_entry.grid(row=1, column=2,  padx=30, pady=(10, 15))

        room_capacity_lbl = customtkinter.CTkLabel(self.update_room_frame, text="Room Capacity",
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        room_capacity_lbl.grid(row=2, column=0, padx=30, pady=(10, 15))
        room_capacity_entry = customtkinter.CTkEntry(self.update_room_frame, width=200,
                                            placeholder_text=f"{self.room_to_be_updated[2]}")
        room_capacity_entry.grid(row=2, column=2, padx=30, pady=(10, 15))
        is_room_active_lbl = customtkinter.CTkLabel(self.update_room_frame, text="Is Room Active ?",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
        is_room_active_lbl.grid(row=3, column=0, padx=30, pady=(10, 15))
        is_room_active_checkbox = customtkinter.CTkCheckBox(self.update_room_frame, text="")
        is_room_active_checkbox.grid(row=3, column=2,  padx=30, pady=(10, 15))

        room_capacity_entry.insert(0, self.room_to_be_updated[2])
        room_name_entry.insert(0, self.room_to_be_updated[1])

        update_room_button = customtkinter.CTkButton(self.update_room_frame, command =  lambda:
                self.update_room(self.room_to_be_updated[0], room_name_entry.get(),
                                  room_capacity_entry.get(),
                                  bool(is_room_active_checkbox.get())),
                                    text="Update Room" ,width=200)

        update_room_button.grid(row=4, column=1, padx=30, pady=(15, 15))

    def load_welcome_frame(self) -> None:
        """ Display Welcome Frame"""
        self.welcome_frame = customtkinter.CTkFrame(self.app, corner_radius=0)
        self.welcome_frame.grid(row=0, column=0, sticky="ns")
        welcome_label = customtkinter.CTkLabel(self.welcome_frame,
            text="Please enter your name", font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.welcome_frame,
                                width=200, placeholder_text="User Name")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        load_main_frame_button = customtkinter.CTkButton(self.welcome_frame,
                                text="Get Started", command = self.welcome_button ,width=200)
        load_main_frame_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def welcome_button(self) -> None:
        """ Display Welcome Frame"""
        print(f"Welcome {self.username_entry.get()}")
        self.welcome_frame.grid_forget()
        self.load_main_frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")

    def run(self):
        """Put everything together"""
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.load_background_image()
        self.load_welcome_frame()
        self.app.mainloop()
