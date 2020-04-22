import pytest

import life


def test_die():
    game = life.GameOfLife(max_x=2, max_y=2, population=0, template="OOOO")
    game.flip()  # need to flip because the next_world isn't initialized with the template yet
    game.die(1, 1)
    game.flip()
    assert game.alive(0, 0)
    assert game.alive(0, 1)
    assert game.alive(1, 0)
    assert not game.alive(1, 1)


def test_live():
    game = life.GameOfLife(max_x=2, max_y=2, population=0, template="")
    game.live(1, 1)
    game.flip()
    assert not game.alive(0, 0)
    assert not game.alive(0, 1)
    assert not game.alive(1, 0)
    assert game.alive(1, 1)


def test_count_neighbours():
    game = life.GameOfLife(max_x=3, max_y=3, population=0, template="")
    game.live(0, 1)
    game.live(1, 0)
    game.live(1, 2)
    game.live(2, 1)
    game.flip()
    # assert game.count_neighbours(0, 0) == 2
    # assert game.count_neighbours(0, 1) == 2
    # assert game.count_neighbours(0, 2) == 2
    # assert game.count_neighbours(1, 0) == 2
    # assert game.count_neighbours(1, 1) == 4
    # assert game.count_neighbours(1, 2) == 2
    # assert game.count_neighbours(2, 0) == 2
    # assert game.count_neighbours(2, 1) == 2
    # assert game.count_neighbours(2, 2) == 2
    assert game.count_neighbours(0, 0) == 4
    assert game.count_neighbours(0, 1) == 3
    assert game.count_neighbours(0, 2) == 4
    assert game.count_neighbours(1, 0) == 3
    assert game.count_neighbours(1, 1) == 4
    assert game.count_neighbours(1, 2) == 3
    assert game.count_neighbours(2, 0) == 4
    assert game.count_neighbours(2, 1) == 3
    assert game.count_neighbours(2, 2) == 4


def test_check_livelihood():
    game = life.GameOfLife(max_x=3, max_y=3, population=0, template="")
    game.live(0, 1)
    game.live(1, 0)
    game.live(1, 2)
    game.flip()
    # assert not game.check_livelihood(0, 0)
    # assert game.check_livelihood(0, 1)
    # assert not game.check_livelihood(0, 2)
    # assert not game.check_livelihood(1, 0)
    # assert game.check_livelihood(1, 1)
    # assert not game.check_livelihood(1, 2)
    # assert not game.check_livelihood(2, 0)
    # assert not game.check_livelihood(2, 1)
    # assert not game.check_livelihood(2, 2)
    assert game.check_livelihood(0, 0)
    assert game.check_livelihood(0, 1)
    assert game.check_livelihood(0, 2)
    assert game.check_livelihood(1, 0)
    assert game.check_livelihood(1, 1)
    assert game.check_livelihood(1, 2)
    assert game.check_livelihood(2, 0)
    assert game.check_livelihood(2, 1)
    assert game.check_livelihood(2, 2)


def test_step_1():
    game = life.GameOfLife(max_x=3, max_y=3, population=0, template="")
    game.live(0, 1)
    game.live(1, 0)
    game.live(1, 2)
    game.flip()
    done = game.step()
    game.flip()
    assert not done
    # assert not game.alive(0, 0)
    # assert game.alive(0, 1)
    # assert not game.alive(0, 2)
    # assert not game.alive(1, 0)
    # assert game.alive(1, 1)
    # assert not game.alive(1, 2)
    # assert not game.alive(2, 0)
    # assert not game.alive(2, 1)
    # assert not game.alive(2, 2)
    assert game.alive(0, 0)
    assert game.alive(0, 1)
    assert game.alive(0, 2)
    assert game.alive(1, 0)
    assert game.alive(1, 1)
    assert game.alive(1, 2)
    assert game.alive(2, 0)
    assert game.alive(2, 1)
    assert game.alive(2, 2)


def test_step_2():
    game = life.GameOfLife(max_x=3, max_y=3, population=0, template="")
    done = game.step()
    game.flip()
    assert done
    assert not game.alive(0, 0)
    assert not game.alive(0, 1)
    assert not game.alive(0, 2)
    assert not game.alive(1, 0)
    assert not game.alive(1, 1)
    assert not game.alive(1, 2)
    assert not game.alive(2, 0)
    assert not game.alive(2, 1)
    assert not game.alive(2, 2)

