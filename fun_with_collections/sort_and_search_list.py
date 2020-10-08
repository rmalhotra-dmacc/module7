"""
Author: Rajiv Malhotra
Program: sort_and_search_list.py
Date: 10/07/20

Search and Sort Assignment
"""


def search_list(u_list, a_value):
    """
    Function searches for a value in the list and returns the index value. -1 if not found
    :param u_list: A list
    :param a_value: A value that is searched in the list
    :return: Either the index value or -1
    :rtype: Int
    """
    try:
        index = u_list.index(a_value)
        return index
    except ValueError:
        return -1


def sort_list(u_list):
    """
    Function sorts the list
    :param u_list: A list
    :return: Sorted list
    :rtype: List
    """
    u_list.sort()
    return u_list  #return was coded to pass back the sorted list


if __name__ == '__main__':
    u_list = ['z', 'e', 'i', 'o', 'u']
    a_value = input("Enter a value to search in the list: ")
    index_value = search_list(u_list, a_value)
    print("Index found: {}".format(index_value))
    print(sort_list(u_list))
