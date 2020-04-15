import os
import random
import sys


class GameOfLife:
    """
    The Game of Life, originally theorized by John H. Conway, is a zero-player game consisting of
    a 2-dimensional map of cells. Each cell has 8 neighbours: 2 horizontal, 2 vertical, and 4 diagonal.
    The game has 2 simple rules:
    - A living cell survives if it has 2 or 3 living neighbours, otherwise it dies.
    - A dead cell becomes alive if it has exactly 3 neighbours, otherwise it stays dead.
    """

    def __init__(
            self,
            max_x=100,
            max_y=100,
            population=2000,
            template=None,
            reach=1,
            wraparound=True,
    ):
        self.max_x = max_x
        self.max_y = max_y
        self.reach = reach
        self.wraparound = wraparound

        self.world = self.create_world(False)
        self.next_world = self.create_world(False)
        self.neighbourhoods = self.create_world(None)

        if population > 0:
            x = random.randint(0, max_x - 1)
            y = random.randint(0, max_y - 1)
            for _ in range(population):
                while self.alive(x, y):
                    x = random.randint(0, max_x - 1)
                    y = random.randint(0, max_y - 1)
                self.set_world_value(self.world, x, y, True)
        else:
            x = 0
            y = 0
            for cell in template:
                if cell == '\n':
                    y = 0
                else:
                    if cell != ' ':
                        self.set_world_value(self.world, x, y, True)
                    y += 1
                    y = y % max_y
                if y == 0:
                    x += 1
                    if x == max_x:
                        break

    def create_world(self, value=False):
        return [[value] * self.max_y for _ in range(self.max_x)]

    @staticmethod
    def set_world_value(world, x, y, value):
        world[x][y] = value

    @staticmethod
    def world_value(world, x, y):
        return world[x][y]

    def die(self, x, y):
        self.set_world_value(self.next_world, x, y, False)

    def live(self, x, y):
        self.set_world_value(self.next_world, x, y, True)

    def alive(self, x, y):
        return self.world_value(self.world, x, y)

    def find_neighbours(self, x, y):
        neighbourhood = self.world_value(self.neighbourhoods, x, y)
        if not neighbourhood:
            neighbourhood = [
                [nx, ny]
                for nx in [x + i for i in range(-self.reach, self.reach + 1)]
                for ny in [y + i for i in range(-self.reach, self.reach + 1)]
                if not (x == nx and y == ny)
            ]
            self.set_world_value(self.neighbourhoods, x, y, neighbourhood)
        return neighbourhood

    def count_neighbours(self, x, y):
        n = 0
        for nx, ny in self.find_neighbours(x, y):
            if not self.wraparound:
                if not 0 <= nx < self.max_x:
                    continue
                if not 0 <= ny < self.max_y:
                    continue
            if self.alive(nx % self.max_x, ny % self.max_y):
                n += 1
        return n

    def check_livelihood(self, x, y):
        neighbours = self.count_neighbours(x, y)
        if self.alive(x, y):
            return (self.reach + 1) <= neighbours <= (self.reach * 3)
        else:
            return neighbours == (1 + (self.reach * 2))

    def step(self):
        output = ""
        for x in range(self.max_x):
            for y in range(self.max_y):
                if self.check_livelihood(x, y):
                    self.live(x, y)
                    output += 'O'
                else:
                    self.die(x, y)
                    output += ' '
            output += '\n'
        os.system('clear')
        print(output)
        return self.next_world == self.world

    def print(self):
        output = ""
        for x in range(self.max_x):
            for y in range(self.max_y):
                if self.alive(x, y):
                    output += 'O'
                else:
                    output += ' '
            output += '\n'
        os.system('clear')
        print(output)

    def flip(self):
        tmp = self.world
        self.world = self.next_world
        self.next_world = tmp


if __name__ == "__main__":  # pragma: no cover
    done = False
    game = GameOfLife()
    while not done:
        done = game.step()
        game.flip()
