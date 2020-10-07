"""
Author: Rajiv Malhotra
Program: basic_list.py
Date: 10/07/20

Basic List Assignment
"""


def make_list():
    u_list = []
    for i in range(0, 3):
        try:
            u_input = int(get_input())
            u_list.insert(i, u_input)
        except ValueError:
            raise ValueError
    return u_list


def get_input():
    u_input = input("Give me a number: ")
    return u_input


if __name__ == '__main__':
    try:
        test_list = make_list()
        print(test_list)
    except ValueError as err:
        print("Please Enter only numbers")
