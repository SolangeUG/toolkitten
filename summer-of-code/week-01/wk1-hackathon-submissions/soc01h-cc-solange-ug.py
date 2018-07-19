#!/usr/bin/env python3

# Global variables
world = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
n = len(world)
tiles_queue = []


def continent_size(start):
    """
    Return the size of the continent which the start tile is part of
    :param start: given starting position/tile is an array of indexes
    :return: the continent size around the input tile
    """
    size = 0
    tiles_queue.append(start)
    while len(tiles_queue) > 0:
        tile = tiles_queue.pop(0)
        i = tile[0]
        j = tile[1]
        if world[i][j] == 1:
            size += 1
            world[i][j] = 0
            check_neighbours(tile)
    return size


def check_neighbours(tile):
    """
    Check if the neighbouring tiles have a desired value (1 in this case)
    and add them to our global variable tiles_queue
    :param tile: input tile as an array of indexes
    :return: None
    """
    x = tile[0]
    y = tile[1]
    for i in range(x - 1, x + 2):
        if (i >= 0) and (i < n):
            for j in range(y - 1, y + 2):
                if (j >= 0) and (j < n):
                    if world[i][j] == 1:
                        tiles_queue.append(list((i, j)))


# TESTS
print("**** Continent size from tile [0, 10] ****")
starting_position = [0, 10]
the_size = continent_size(starting_position)
print('our continent size is ' + str(the_size))
