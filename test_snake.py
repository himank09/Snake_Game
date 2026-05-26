"""Unit tests for snake game logic."""

import unittest
from snake_game import Snake
from food  import Food
from game  import Game


class TestSnake(unittest.TestCase):

    def test_initial_position(self):
        snake = Snake(grid_size=20)
        self.assertEqual(len(snake.body), 3)
        self.assertTrue(snake.alive)
        self.assertEqual(snake.score, 0)

    def test_move_right(self):
        snake = Snake(grid_size=20)
        head_before = snake.body[0]
        snake.step((-1, -1))  # food far away
        head_after = snake.body[0]
        self.assertEqual(head_after[0], head_before[0] + 1)
        self.assertEqual(head_after[1], head_before[1])

    def test_cannot_reverse(self):
        snake = Snake(grid_size=20)
        snake.change_direction((-1, 0))  # try to go left while moving right
        self.assertEqual(snake.next_dir, (1, 0))  # direction unchanged

    def test_wall_collision(self):
        snake = Snake(grid_size=5)
        snake.body = [(4, 2), (3, 2), (2, 2)]
        snake.direction = (1, 0)
        snake.next_dir  = (1, 0)
        snake.step((-1, -1))
        self.assertFalse(snake.alive)

    def test_self_collision(self):
        snake = Snake(grid_size=20)
        snake.body = [(5,5),(5,6),(5,7),(5,8),(4,8),(4,7),(4,6),(4,5),(4,4),(5,4),(6,4),(6,5),(6,6),(6,7),(6,8)]
        snake.direction = (0, -1)
        snake.next_dir  = (0, -1)
        snake.step((-1, -1))
        self.assertFalse(snake.alive)

    def test_eat_food_grows(self):
        snake = Snake(grid_size=20)
        head  = snake.body[0]
        food_pos = (head[0] + 1, head[1])
        length_before = len(snake.body)
        snake.step(food_pos)
        self.assertEqual(len(snake.body), length_before + 1)

    def test_score_increases(self):
        snake = Snake(grid_size=20)
        head  = snake.body[0]
        food_pos = (head[0] + 1, head[1])
        snake.step(food_pos)
        self.assertGreater(snake.score, 0)

    def test_food_not_on_snake(self):
        game = Game(grid_size=20)
        self.assertNotIn(game.food.position, game.snake.body)

    def test_restart(self):
        game = Game(grid_size=20)
        game.snake.alive = False
        game.restart()
        self.assertTrue(game.snake.alive)
        self.assertEqual(game.snake.score, 0)


if __name__ == "__main__":
    unittest.main()