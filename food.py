"""
Food logic — places food randomly on the grid,
making sure it never spawns inside the snake.
"""

import random


class Food:
    def __init__(self, grid_size=20):
        self.grid_size = grid_size
        self.position  = (0, 0)

    def place(self, snake_body):
        """Place food at a random empty cell."""
        empty_cells = [
            (x, y)
            for x in range(self.grid_size)
            for y in range(self.grid_size)
            if (x, y) not in snake_body
        ]
        self.position = random.choice(empty_cells)