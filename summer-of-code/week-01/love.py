#!/usr/bin/env python3
# Love Affair


def words_and_indices():
    print("**** Working with words and indices ****")
    name = "Rebecca Fillier"
    result = ""
    print('result: ' + result)
    print(name[1])
    i = 1
    print(name[i])
    for i in range(0, 15):
        print(name[i])


def words_indices_and_size():
    print("**** Working with words, indices and size ****")
    result = ""
    name = "Rebecca Fillier"
    print(len(name))
    for i in range(0, len(name)):
        print(name[i])
        if i % 2 == 0:
            print(name[i])
            result = result + name[i]
            print('result just changed to: ' + result)
    print('The final result for all even indexed letters in name is: '
          + result
          + '! Drumroll please!!! Thank you. I would like to thank the Academy. (Little bow)')


def words_and_negative_or_out_of_range_indices():
    print("**** Working with words, negative and out of range indices ****")
    name = "Rebecca Fillier"
    print(name[-1])
    # print(name[15]) --> EXCEPTION
    # print(name[-15]) --> EXCEPTION


# TESTS
print()
words_and_indices()

print()
words_indices_and_size()

print()
words_and_negative_or_out_of_range_indices()

