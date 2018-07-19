#!/usr/bin/env python3


def working_with_numbers():
    print("**** Working with numbers ****")
    print(1 + 2)
    print(3)
    print(10 % 2)
    print(11 % 2)


def bitshifting():
    print("**** Bitshifting ****")
    for i in range(0, 9):
        print("bitshift ", i, "times ", 1 << i)


def working_with_strings():
    print("**** Working with strings ****")
    print('Hello, world!')
    print('')
    print('Good-bye.')
    print( 'I like' + 'chocolate cake.' )
    print('I like ' + 'apple pie.')
    print('I like' + ' apple pie.')


def more_strings():
    print("**** More strings and an exception ****")
    print('blink ' * 4)
    print('moo' * 3)
    # print('moo' / 3) --> EXCEPTION


def diff_numbers_strings():
    print("**** Working with numbers and strings ****")
    print(12 + 12)
    print('12' + '12')
    print('12 + 12')
    print(2 * 5)
    print('2' * 5)
    print('2 * 5')
    print('12' + str(12))
    # print('12' + 12) --> EXCEPTION
    # print('2' * '5') --> EXCEPTION


def advanced_string_operations():
    print("**** Advanced string operations ****")
    print('You\'re swell!')
    print('backslash at the end of a string: \\')
    print('up\\down')
    print('up\down')
    # print('Betty' + 12) --> EXCEPTION
    # print('Francesca' * 'Hanna') --> EXCEPTION


# TESTS
print()
working_with_numbers()

print()
bitshifting()

print()
working_with_strings()

print()
more_strings()

print()
diff_numbers_strings()

print()
advanced_string_operations()
