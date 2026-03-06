import os
from tkinter import Image
from PIL import Image
import customtkinter


class UserInterface():
    width = 800
    height = 600

    def __init__(self):
        self.new_room_frame = None
        self.welcome_frame = None
        self.main_frame = None
        self.username_entry = None
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.app = customtkinter.CTk()
        self.app.geometry(f"{self.width}x{self.height}")
        self.app.title("Room Booking Application")
        self.app.resizable(width=False, height=False)
        self.username = None

    def load_background_image(self):
        current_path = os.path.dirname(__file__)
        image = customtkinter.CTkImage(Image.open(current_path + "/images/nature.png"), size=(self.width,self.height))
        background_image = customtkinter.CTkLabel(self.app,image=image)
        background_image.grid(row=0,column=0)

    def load_main_frame(self):
        self.main_frame = customtkinter.CTkFrame(master=self.app)
        self.main_frame.grid_columnconfigure(0, weight=1)
        welcome_label = customtkinter.CTkLabel(self.main_frame, text = f"Welcome {self.username_entry.get()}",
                                             font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome_label.grid(row=0, column=0, padx=30, pady=(5, 5))
        intro_label =customtkinter.CTkLabel(self.main_frame, text = f"List of All rooms",
                                             font=customtkinter.CTkFont(size=20))
        intro_label.grid(row=1, column=0, padx=30, pady=(5, 5))

        add_new_room_button = customtkinter.CTkButton(self.main_frame, text="Add a new Room" ,command = self.add_new_room ,width=200)
        add_new_room_button.grid(row=3, column=0, padx=30, pady=(15, 15))
    def add_new_room(self):
        self.main_frame.grid_forget()
        self.load_add_room_frame()
        self.new_room_frame.grid(row=0, column=0, sticky="nsew")

    def load_add_room_frame(self):
        self.new_room_frame = customtkinter.CTkFrame(master=self.app)
        welcome_label = customtkinter.CTkLabel(self.new_room_frame, text="Adding a new room",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome_label.grid(row=0, column=1, padx=30, pady=(100, 15))

        room_name_label = customtkinter.CTkLabel(self.new_room_frame, text="Room Name",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        room_name_label.grid(row=1, column=0, padx=30, pady=(10, 15))
        room_name_entry = customtkinter.CTkEntry(self.new_room_frame, width=200, placeholder_text="Room Name")
        room_name_entry.grid(row=1, column=2,  padx=30, pady=(10, 15))

        room_capacity_label = customtkinter.CTkLabel(self.new_room_frame, text="Room Capacity",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        room_capacity_label.grid(row=2, column=0, padx=30, pady=(10, 15))
        room_capacity_entry = customtkinter.CTkEntry(self.new_room_frame, width=200, placeholder_text="Room Capacity")
        room_capacity_entry.grid(row=2, column=2, padx=30, pady=(10, 15))

        is_room_active_label = customtkinter.CTkLabel(self.new_room_frame, text="Is Room Active ?",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
        is_room_active_label.grid(row=3, column=0, padx=30, pady=(10, 15))
        is_room_active_checkbox = customtkinter.CTkCheckBox(self.new_room_frame, text="")
        is_room_active_checkbox.grid(row=3, column=2,  padx=30, pady=(10, 15))

        add_room_button = customtkinter.CTkButton(self.new_room_frame, text="Add Room" ,width=200)
        add_room_button.grid(row=4, column=1, padx=30, pady=(15, 15))



    def load_welcome_frame(self):
        self.welcome_frame = customtkinter.CTkFrame(self.app, corner_radius=0)
        self.welcome_frame.grid(row=0, column=0, sticky="ns")
        welcome_label = customtkinter.CTkLabel(self.welcome_frame, text="Please enter your name",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        welcome_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.welcome_frame, width=200, placeholder_text="User Name")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        load_main_frame_button = customtkinter.CTkButton(self.welcome_frame, text="Get Started", command = self.welcome_button ,width=200)
        load_main_frame_button.grid(row=3, column=0, padx=30, pady=(15, 15))


    def welcome_button(self):
        print(f"Welcome {self.username_entry.get()}")
        self.welcome_frame.grid_forget()
        self.load_main_frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")



    def run(self):
        self.load_background_image()
        self.load_welcome_frame()
        self.app.mainloop()