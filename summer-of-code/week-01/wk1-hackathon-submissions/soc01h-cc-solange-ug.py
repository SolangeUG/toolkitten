#!/usr/bin/env python3

import random

# Global variables
tiles_queue = []


def random_world_generator(n):
    """
    Randomly generate a world of size n
    :param n: desired size for the world to be generated
    :return: a randomly generated world
    """
    row = [0 for x in range(n)]
    random_world = [row for y in range(n)]
    for i in range(n):
        for j in range(n):
            value = random.randint(0, 1)
            random_world[i][j] = value
    return random_world


def continent_size(grid, start):
    """
    Return the size of the continent which the start tile is part of
    :param grid: given world that contains the start position
    :param start: given starting position/tile is an array of indexes
    :return: the continent size around the input tile
    """
    size = 0
    n = len(grid)
    # make sure the starting position is within the grid/world bounds
    if (start[0] >= 0) and (start[0] < n) \
            and (start[1] >= 0) and (start[1] < n):
        tiles_queue.append(start)
        while len(tiles_queue) > 0:
            tile = tiles_queue.pop(0)
            i = tile[0]
            j = tile[1]
            if grid[i][j] == 1:
                size += 1
                grid[i][j] = 0
                check_neighbours(grid, tile)
    return size


def check_neighbours(grid, tile):
    """
    Check if the neighbouring tiles have a desired value (1 in this case)
    and add them to our global variable tiles_queue
    :param grid: input world that contains the tile in question
    :param tile: input tile as an array of indexes
    :return: None
    """
    x = tile[0]
    y = tile[1]
    n = len(grid)
    for i in range(x - 1, x + 2):
        if (i >= 0) and (i < n):
            for j in range(y - 1, y + 2):
                if (j >= 0) and (j < n):
                    if grid[i][j] == 1:
                        tiles_queue.append(list((i, j)))


def print_grid(grid):
    """
    Print the given grid in a readable form
    :param grid: input grid/world to be printed
    """
    print('[')
    for row in grid:
        print(row, ',')
    print(']')


# ########### TESTS ##########
print("**** **** **** **** **** **** **** ****")
world = random_world_generator(14)
print_grid(world)
starting_position = [5, 7]
the_size = continent_size(world, starting_position)
print('Continent size is ', the_size)

