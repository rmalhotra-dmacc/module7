"""
Author: Rajiv Malhotra
Program: basic_IO.py
Date: 10/09/20

File I/O using Tuples Assignment.
"""

FILE_NAME = 'student_info.txt'
IOERROR_MSG = 'Cannot open file on file system'
MIN = 1
MAX = 50


def write_to_file(*args):
    """
    Function accepts a tuple to be added to the end of a file
    :param args: tuple
    :return: None
    """
    try:
        with open(FILE_NAME, 'a') as f:
            f.write('{}, {}:\t'.format(args[1], args[0]))
            for i in args[2]:
                f.write('{}\t'.format(i))
            f.write('\n')
    except IOError:
        print(IOERROR_MSG)


def get_student_info(**kwargs):
    """
    Function accepts arguments for student name, prompts user to input as many test scores
    :param kwargs: Keyword argument for student name
    :return: None
    """
    print("Welcome, {} {}".format(kwargs['first_name'], kwargs['last_name']))
    scores = []
    num = 0
    while num != -1:
        try:
            num = float(input("Enter a score between {} and {}, (-1 to exit)".format(MIN, MAX)))
            if num == -1:
                break
            elif num < MIN or num > MAX:
                raise ValueError("Score must be between {} and {}".format(MIN, MAX))
            else:
                scores.append(num)
        except ValueError as err:
            print(err)
    write_to_file(kwargs['first_name'], kwargs['last_name'], scores)


def read_from_file():
    try:
        with open(FILE_NAME, 'r') as f:
            read_line = f.read()
            print(read_line)
    except IOError:
        print(IOERROR_MSG)


if __name__ == '__main__':
    get_student_info(first_name='Rajiv', last_name='Malhotra')
    get_student_info(first_name='Bob', last_name='Morgan')
    get_student_info(first_name='Bill', last_name='Johnson')
    get_student_info(first_name='Kent', last_name='Hinnen')
    input("Hold . . . .")
    read_from_file()
    input('Press any key to end')
