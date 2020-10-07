"""
Author: Rajiv Malhotra
Program: basic_list_exception.py
Date: 10/07/20

Basic List Exception Assignment
"""


INPUT_MSG = "Enter a number between 1 and 50 only: "
ERROR_MSG = "Sorry, Number must be between 1 & 50"


def make_list():
    """
    Make list function
    :return: List of 3 numbers
    """
    u_list = []
    for i in range(0, 3):
        try:
            u_input = int(get_input())
            if u_input < 1 or u_input > 50:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            u_list.insert(i, u_input)
    return u_list


def get_input():
    u_input = input(INPUT_MSG)
    return u_input


if __name__ == '__main__':
    try:
        test_list = make_list()
        print(test_list)
    except ValueError as err:
        print(ERROR_MSG)
