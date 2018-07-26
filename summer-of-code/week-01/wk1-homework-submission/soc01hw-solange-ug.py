#!/usr/bin/env python3


def hours_in_year(year):
    """
    Return the number of hours in given year
    :param year: input year parameter
    :return: the number of hours in input year
    """
    days = 365
    if is_leap_year(year):
        days += 1
    return 24 * days


def is_leap_year(year):
    """
    Determine whether the input year is leap or not
    :param year: input year parameter
    :return: true if the input year is leap, false otherwise
    """
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


def minutes_in_decade():
    """
    Return the number of minutes in a decade
    :return: minutes in 10 years
    """
    years_in_decade, days_in_year = 10, 365
    hours_in_day, minutes_in_hour = 24, 60
    return years_in_decade * days_in_year * hours_in_day * minutes_in_hour


def age_in_seconds(age):
    """
    Return age in seconds from an input age in years
    :param age: input age (in years) parameter
    :return: age in seconds
    """
    days_in_year, hours_in_day = 365, 24
    minutes_in_hour, seconds_in_minute = 60, 60
    return age * days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute


def precise_age_in_seconds():
    """
    Return a precise computation of my age in seconds
    :return: my age in seconds
    """
    from datetime import datetime

    difference = datetime.now() - datetime(1983, 4, 17, 3)
    hours_in_day, seconds_in_hour = 24, 3600
    return difference.days * hours_in_day * seconds_in_hour + difference.seconds


def processor_timeout(processor):
    """
    Return the number of days a given processor (32-bit or 64-bit)
    will take to time out if it has an integer overflow bug
    :param processor: 32-bit or 64-bit machine
    :return: number of days it takes to time out
    """
    hours_in_day = 24
    highest_integer = 2**31 - 1
    if processor == 64:
        highest_integer = 2**63 - 1
    timeout_in_days = highest_integer / (1 / hours_in_day)
    return timeout_in_days


def fullname_greeting():
    """
    Return a greeting with a person's fullname
    :return: fullname greeting
    """
    firstname = input('Please enter your firstname: ')
    middlename = input('Please enter your middlename: ')
    lastname = input('Please enter your lastname: ')
    return 'Good morning ' + firstname + ' ' + middlename + ' ' + lastname + '!'


def bigger_better_number():
    """
    Suggest a bigger, better favorite number to the user
    :return: user's favorite number + 1
    """
    number = input('What is your favorite number? ')
    while not number.isdigit():
        number = input('What is your favorite number? ')
    return int(number) + 1


def angry_boss_program():
    """
    Return an angry boss response to an employee demand
    :return: angry boss response
    """
    wish = input('What do you want? ')
    return 'WHADDAYA MEAN "' + wish.upper() + '"?!? YOU\'RE FIRED!!'


def table_of_contents_formatter():
    """
    Display a formatted table of contents using center, ljust and rjust functions
    :return: a formatted table of contents
    """
    contents = "Table of Contents \n" \
        + "Chapter 1 ".ljust(1) + "Getting Started".center(30) + "page 1".rjust(7) + "\n" \
        + "Chapter 2 ".ljust(1) + "Numbers".center(22) + "page 9".rjust(15) + "\n" \
        + "Chapter 3 ".ljust(1) + "Letters".center(22) + "page 13".rjust(16)
    return contents


def ninety_nine_bottles():
    """
    Return the lyrics to that beloved classic 99 Bottles of Beer on the Wall
    :return: 99 Bottles of Beer on the Wall lyrics
    """
    bottles = 99
    lyrics = ''
    while bottles > 0:
        lyrics += str(bottles) + ' bottles of beer on the wall, ' + str(bottles) + ' bottles of beer.\n' \
                    + 'Take one down and pass it around, ' + str(bottles - 1) + ' bottles of beer on the wall.\n\n'
        bottles -= 1

    bottles = 99
    lyrics += 'No more bottles of beer on the wall, no more bottles of beer.\n' \
              + 'Go to the store and buy some more, ' + str(bottles) + ' bottles of beer on the wall.\n\n'
    return lyrics


def deaf_grandma():
    """
    Whatever is entered by the user, this should output HUH?! SPEAK UP, GIRL!
    Unless, it's typed in all capital letters. Then, the output should be NO, NOT SINCE YYYY,
    where YYYY is between 1938 and 1950.
    The function terminates when the user inputs BYE.
    :return: deaf grandma's response
    """
    import random

    question = input('Ask Grandma questions:\n ')
    while True:
        if not question.isupper():
            question = input('HUH?! SPEAK UP, GIRL!\n ')
        else:
            if question != 'BYE':
                year = 1938 + random.randrange(0, 13)
                question = input('NO, NOT SINCE ' + str(year) + '!\n ')
            else:
                return


def leap_years_in_between(start, end):
    """
    Return all the leap years in between two input years, and including start and end years if they're leap years
    :param start: input starting year
    :param end: input end year
    :return: all leap years in between
    """
    leap_years = []
    for year in range(start, end + 1):
        if is_leap_year(year):
            leap_years.append(year)
    return leap_years


def word_sorter():
    """
    Sort and return a list of input words from the user
    :return: a sorted list of words provided by a user
    """
    words = []
    print('Enter words of your choice, one word per line.\nPress ENTER on an epmty line to terminate the list.')
    word = 'word'
    while word != '':
        word = input()
        if word != '':
            words.append(word)
    words.sort()
    return words


def old_school_roman(number):
    """
    Return the old-school roman numeral equivalent to the input number
    :param number: input number to be converted
    :return: equivalent old-school roman numeral
    """
    # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    divisors = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

    d = number
    numeral = ''
    for key, value in divisors.items():
        d = int(d / key)
        if d > 0:
            for i in range(0, d):
                numeral += value
        d = number % key
    return numeral


def new_style_roman(number):
    """
    Return the new-style roman numeral equivalent to the input number
    :param number: input number to be converted
    :return: equivalent new-style roman numeral
    """
    divisors = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    next_value = {'I': 'X', 'X': 'L', 'C': 'M'}

    d = number
    numeral = ''
    for key, value in divisors.items():
        d = int(d / key)
        if 0 < d <= 3:
            for i in range(0, d):
                numeral += value
        elif d > 3:
            if key == 100:
                next_val = 'D'
            else:
                next_val = next_value[value]
            numeral += value
            numeral += next_val
        d = number % key
    return numeral


"""
###############################################################################################
                                            TESTS
###############################################################################################
"""
# year = 2018
# result = hours_in_year(year)
# print('\nThere\'re', result, 'hours in year ', year, '\n')
#
# result = minutes_in_decade()
# print('There\'re', result, 'minutes in a decade\n')
#
# your_age = 35
# result = age_in_seconds(your_age)
# print('Your age in seconds is', result, '\n')
#
# archi = 32
# result = processor_timeout(archi)
# print('A 32-bit processor will time out in', result, 'days\n')
#
# result = fullname_greeting()
# print(result, '\n')
#
# result = bigger_better_number()
# print('Bigger, better number suggestion:', result, '\n')
#
# result = angry_boss_program()
# print(result, '\n')
#
# result = table_of_contents_formatter()
# print(result, '\n')
#
# result = ninety_nine_bottles()
# print(result)
#
# deaf_grandma()
#
# start_year = 1988
# end_year = 2025
# result = leap_years_in_between(start_year, end_year)
# print('\n', result, '\n')
#
# result = word_sorter()
# print(result, '\n')
#
# input_number = 48
# result = old_school_roman(input_number)
# print(input_number, 'is equivalent to', result, 'in old-school roman numeral notation')

input_number = 900
result = new_style_roman(input_number)
print(input_number, 'is equivalent to', result, 'in new-style roman numeral notation')
