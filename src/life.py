import os
import random
import sys
import time


REACH = 1
NEIGHBOURHOODS = []


def die(world, x, y):
    world[x][y] = False


def live(world, x, y):
    world[x][y] = True


def alive(world, x, y):
    return world[x][y]


def find_neighbours(x, y):
    neighbourhood = NEIGHBOURHOODS[x][y]
    if not neighbourhood:
        neighbourhood = [
            [nx, ny]
            for nx in [x + i for i in range(-REACH, REACH + 1)]
            for ny in [y + i for i in range(-REACH, REACH + 1)]
            if not (x == nx and y == ny)
        ]
        NEIGHBOURHOODS[x][y] = neighbourhood
    return neighbourhood


def count_neighbours(world, x, y):
    n = 0
    max_x = len(world)
    max_y = len(world[0])
    for nx, ny in find_neighbours(x, y):
        # if not 0 <= nx < max_x:
        #     continue
        # if not 0 <= ny < max_y:
        #     continue
        if alive(world, nx % max_x, ny % max_y):
            n += 1
    return n


def check_livelihood(world, x, y):
    neighbours = count_neighbours(world, x, y)
    if alive(world, x, y):
        return (REACH + 1) <= neighbours <= (REACH * 3)
    else:
        return neighbours == (1 + (REACH * 2))


def step(world, new_world):
    output = ""
    for x in range(len(world)):
        for y in range(len(world[x])):
            if check_livelihood(world, x, y):
                live(new_world, x, y)
                output += 'O'
            else:
                die(new_world, x, y)
                output += ' '
        output += '\n'
    os.system('clear')
    print(output)
    return new_world == world


def first_world(max_x=100, max_y=200, population=1000, template=""):
    max_x = int(max_x)
    max_y = int(max_y)
    population = int(population)
    world = [[False] * max_y for _ in range(max_x)]
    next_world = [[False] * max_y for _ in range(max_x)]
    neighbourhoods = [[None] * max_y for _ in range(max_x)]
    if population > 0:
        x = random.randint(0, max_x - 1)
        y = random.randint(0, max_y - 1)
        for _ in range(population):
            while alive(world, x, y):
                x = random.randint(0, max_x - 1)
                y = random.randint(0, max_y - 1)
            live(world, x, y)
    else:
        x = 0
        y = 0
        for cell in template:
            if cell == '\n':
                y = 0
            else:
                if cell != ' ':
                    live(world, x, y)
                y += 1
                y = y % max_y
            if y == 0:
                x += 1
                if x == max_x:
                    break
    return world, next_world, neighbourhoods


if __name__ == "__main__":  # pragma: no cover
    done = False
    current_world, new_world, NEIGHBOURHOODS = first_world(*sys.argv[1:])
    while not done:
        done = step(current_world, new_world)
        tmp = current_world
        current_world = new_world
        new_world = tmp

