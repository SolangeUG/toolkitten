#!/usr/bin/env python3

import random
import time

# Global variables
tiles_queue = []


def random_world_generator(n):
    """
    Randomly generate a world of size n
    :param n: desired size for the world to be generated
    :return: a randomly generated world
    """
    random_world = [[0] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            value = random.randint(0, 1)
            random_world[i][j] = value
    return random_world


def compute_all_continents_sizes(grid):
    """
    Given a world, compute all its continents sizes
    :param grid: given world
    :return: a dictionary that associates each continent with its size
    """
    counter = 0
    result = {}
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                counter += 1
                size = continent_size(grid, list((i, j)))
                result['continent ' + str(counter)] = size
    return result


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
                # mark this element as "already treated"
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
        print('\t', row, ',')
    print(']')


""" 
#################################################################################
                                    PROGRAM
#################################################################################
"""
print()
world_size = input('Enter valid number for size of world to generate: ')
while not world_size.isdigit():
    world_size = input('Enter valid number for size of world to generate: ')
world_size = int(world_size)

# benchmark: measure time taken by program to run
start_time = time.process_time()

world = random_world_generator(world_size)
# uncomment the following line to display randomly generated world
# print_grid(world)
sizes = compute_all_continents_sizes(world)
print('\rAll continents sizes:', sizes)

elapsed_time = time.process_time() - start_time
print('Program running time:', "{:10.20f}".format(elapsed_time), 'seconds.')


