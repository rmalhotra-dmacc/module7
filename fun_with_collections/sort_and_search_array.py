"""
Author: Rajiv Malhotra
Program: sort_and_search_array.py
Date: 10/11/20

Search and Sort Array Assignment
"""

import array as arr


def search_array(n_array, a_value):
    """
    Function searches for a value in the Array and returns the index value. -1 if not found
    :param n_array: An Array
    :param a_value: A value that is searched in the Array
    :return: Either the index value or -1
    :rtype: Int
    """
    try:
        index = n_array.index(a_value)
        return index
    except ValueError:
        return -1


def sort_array(n_array):
    """
    Function sorts the Array
    :param n_array: An Array
    :return: Sorted Array
    :rtype: Array
    """
    print(n_array)
    for i in range(0, len(n_array)):
        for j in range(i+1, len(n_array)):
            if n_array[i] > n_array[j]:
                temp = n_array[i]
                n_array[i] = n_array[j]
                n_array[j] = temp
    return n_array   #return was coded to pass back the sorted Array


if __name__ == '__main__':
    n_array = arr.array('i', [1, 4, 5, 3, 2])
    a_value = int(input("Enter a value to search in the array: "))
    index_value = search_array(n_array, a_value)
    print("Index found: {}".format(index_value))
    print(sort_array(n_array))
