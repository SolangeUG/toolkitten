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


""" 
###############################################################################################
                                            PROGRAM
###############################################################################################
"""
print()
print('There\'re', hours_in_year(2018), 'hours in year 2018')

print()
print('There\'re', minutes_in_decade(), 'minutes in a decade')

print()
your_age = 35
print('Your my age in seconds is', age_in_seconds(your_age))

print()
print('A 32-bit processor will time out in', processor_timeout(32), 'days')

print()
print(fullname_greeting())

print()
print(bigger_better_number())

print()
print(angry_boss_program())

print()
print(table_of_contents_formatter())
