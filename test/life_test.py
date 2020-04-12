import pytest

import life


def create_world(max_x, max_y, value=False):
    return [[value] * max_y for _ in range(max_x)]


def test_die():
    world = create_world(2, 2, True)
    life.die(world, 1, 1)
    assert world[0][0]
    assert world[0][1]
    assert world[1][0]
    assert not world[1][1]


def test_live():
    world = create_world(2, 2, False)
    life.live(world, 1, 1)
    assert not world[0][0]
    assert not world[0][1]
    assert not world[1][0]
    assert world[1][1]


def test_alive():
    world = create_world(2, 2, False)
    life.live(world, 1, 1)
    assert not life.alive(world, 0, 0)
    assert not life.alive(world, 0, 1)
    assert not life.alive(world, 1, 0)
    assert life.alive(world, 1, 1)


def test_count_neighbours():
    world = create_world(3, 3, False)
    life.live(world, 0, 1)
    life.live(world, 1, 0)
    life.live(world, 1, 2)
    life.live(world, 2, 1)
    # assert life.count_neighbours(world, 0, 0) == 2
    # assert life.count_neighbours(world, 0, 1) == 2
    # assert life.count_neighbours(world, 0, 2) == 2
    # assert life.count_neighbours(world, 1, 0) == 2
    # assert life.count_neighbours(world, 1, 1) == 4
    # assert life.count_neighbours(world, 1, 2) == 2
    # assert life.count_neighbours(world, 2, 0) == 2
    # assert life.count_neighbours(world, 2, 1) == 2
    # assert life.count_neighbours(world, 2, 2) == 2
    assert life.count_neighbours(world, 0, 0) == 4
    assert life.count_neighbours(world, 0, 1) == 3
    assert life.count_neighbours(world, 0, 2) == 4
    assert life.count_neighbours(world, 1, 0) == 3
    assert life.count_neighbours(world, 1, 1) == 4
    assert life.count_neighbours(world, 1, 2) == 3
    assert life.count_neighbours(world, 2, 0) == 4
    assert life.count_neighbours(world, 2, 1) == 3
    assert life.count_neighbours(world, 2, 2) == 4


def test_check_livelihood():
    world = create_world(3, 3, False)
    life.live(world, 0, 1)
    life.live(world, 1, 0)
    life.live(world, 1, 2)
    # assert not life.check_livelihood(world, 0, 0)
    # assert life.check_livelihood(world, 0, 1)
    # assert not life.check_livelihood(world, 0, 2)
    # assert not life.check_livelihood(world, 1, 0)
    # assert life.check_livelihood(world, 1, 1)
    # assert not life.check_livelihood(world, 1, 2)
    # assert not life.check_livelihood(world, 2, 0)
    # assert not life.check_livelihood(world, 2, 1)
    # assert not life.check_livelihood(world, 2, 2)
    assert life.check_livelihood(world, 0, 0)
    assert life.check_livelihood(world, 0, 1)
    assert life.check_livelihood(world, 0, 2)
    assert life.check_livelihood(world, 1, 0)
    assert life.check_livelihood(world, 1, 1)
    assert life.check_livelihood(world, 1, 2)
    assert life.check_livelihood(world, 2, 0)
    assert life.check_livelihood(world, 2, 1)
    assert life.check_livelihood(world, 2, 2)


def test_step_1():
    world = create_world(3, 3, False)
    life.live(world, 0, 1)
    life.live(world, 1, 0)
    life.live(world, 1, 2)
    world, done = life.step(world)
    assert not done
    assert world == [
        # [0, 1, 0],
        # [0, 1, 0],
        # [0, 0, 0],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]


def test_step_2():
    world = create_world(3, 3, False)
    world, done = life.step(world)
    assert done
    assert world == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

