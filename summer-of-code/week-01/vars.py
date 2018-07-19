#!/usr/bin/env python3


def using_variables():
    print("**** Using variables ****")
    a = '...you can say that again...'
    print(a)
    name = 'Darlyze Calixte'
    print('My name is ' + name + '.')
    print('Wow ' + name)
    print(name + ' is a really beautiful name!')


def reusing_variables():
    print("**** Reusing variables ****")
    composer = 'Mozart'
    print(composer)
    composer = 'Tchaikovsky'
    print('But I prefer ' + composer + ', personally.')


def composing_variables():
    print("**** Composing variables ****")
    username = 'Tikwiza' + '-vip'
    print(username)
    score = 5 * (1 + 8)
    print(score)


def substituting_variables():
    print("**** Substituting variables ****")
    old = 8
    new = old
    print(old)
    print(new)
    print('')
    old = 'eight cats'
    print(old)
    print(new)


def using_arrays():
    print("**** Using arrays ****")
    world01 = 'oooooxxoooo'
    world02 = 'oooooxooooo'
    world03 = 'oooooxxoooo'
    world04 = 'oooooxooooo'
    world05 = 'oooxxxooooo'
    world06 = 'oooxoxxoooo'
    world07 = 'ooooxxooooo'
    world08 = 'oooooxxoooo'
    world09 = 'oooooxooooo'
    world10 = 'oooooxooooo'
    world11 = 'oooooxxoooo'
    world = world01 + world02 + world03 + world04 \
        + world05 + world06 + world07 + world08 \
        + world09 + world10 + world11
    print(world)

    # 1-dimensional array
    world = ['o', 'x', 'o']
    print(world[0])
    print(world[2])

    # an array of arrays
    world = [['o', 'x', 'o'],
             ['o', 'x', 'o'],
             ['o', 'x', 'o']]
    print(world[1][1])


# TESTS
print()
using_variables()

print()
reusing_variables()

print()
composing_variables()

print()
substituting_variables()

print()
using_arrays()
