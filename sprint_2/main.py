"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
Project1 Spring 2
File: display_data.py
Purpose: This file contains the 'DisplayDataInTerminal' class that has the methods
that test the "RoomBooking's" methods
"""

from display_data import DisplayDataInTerminal


def main():
    """
    Puts everything together
    :return: None
    """
    instance = DisplayDataInTerminal()
    instance.display_all_my_booking()


if __name__ == '__main__':
    main()
