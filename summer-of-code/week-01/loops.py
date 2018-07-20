#!/usr/bin/env python3
# Loops


def loop_through_input_01():
    print("**** Looping through user input 01 ****")
    text = ""
    while text != "bye":
        text = input("say something please: ")
        print("you said " + text + ".")
        if text == "bye":
            print("good bye to you too")
            break


def loop_through_input_02():
    print("**** Looping through user input 02 ****")
    text = ""
    while text != "bye":
        text = input("say something please : ")
        print("You said \"" + text + "\".")
        print('You said "' + text + '".')
    print("good bye to you too")


def loop_through_numbers():
    print("**** Looping through numbers ****")
    i = 1
    while i < 11:
        print(i)
        i = i + 1
    j = 0
    while j < 11:
        print(j)
        if j == 3:
            break
        j += 1


def loop_through_a_range():
    print("**** Looping through a range of numbers ****")
    for x in range(10):
        print(x)
    for x in range(5, 10):
        print(x)
    for x in range(5, 50, 3):
        print(x)


def loop_through_students():
    print("**** Looping through a list ****")
    students = ["Rocio Pena", "Kat Burkinshaw", "Archana Kumari", "Christina Tarantino",
                "Jessi_RS", "Elle J", "Libi", "T. Pspisilova", "F. Margharita Wailes-Fairbairn"]
    for s in students:
        print(s)

    for s in students:
        if len(s) > 7:
            print(s + " is an amazing Pythonista and has a very long name!")
        if len(s) > 20:
            print("Supercalifragilisticexpialidocious!")
        elif len(s) == 6:
            print(s + " is an amazing Pythonista and has a name that's exactly 6 characters long!")
        elif len(s) == 8:
            print(s + " is an amazing Pythonista and has a name that's exactly 8 characters long!")
        else:
            print(s + " is an amazing Pythonista and a minimalist!")


def list_comprehension():
    print("**** Using list comprehensions ****")
    students = ["Rocio Pena", "Kat Burkinshaw", "Archana Kumari", "Christina Tarantino",
                "Jessi_RS", "Elle J", "Libi", "T. Pspisilova", "F. Margharita Wailes-Fairbairn"]
    usernames = [print(s) for s in students]
    print(usernames)
    usernames = [s+"@1mwtt" for s in students]
    print(usernames)


def other_list_operations():
    print("**** More list operations ****")
    students = ["Rocio Pena", "Kat Burkinshaw", "Archana Kumari", "Christina Tarantino", "Jessi_RS", "Elle J", "Libi",
                "T. Pspisilova", "F. Margharita Wailes-Fairbairn", "Marta Bodojra"]
    print(students)

    students.pop()
    print(students)

    students.sort()
    print(students)

    fruits = ["orange", 2, "kiwi", {}]
    print(fruits)


def real_array():
    print("**** Creating a real array with numpy ****")
    import numpy
    a = numpy.array([1, 2, 3])
    print(len(a))


""" 
###############################################################################################
                                            TESTS
###############################################################################################
"""
print()
loop_through_input_01()

print()
loop_through_input_02()

print()
loop_through_numbers()

print()
loop_through_a_range()

print()
loop_through_students()

print()
list_comprehension()

print()
other_list_operations()

print()
real_array()
