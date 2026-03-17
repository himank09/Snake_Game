"""
Snake game logic — no graphics, pure Python.
This module handles all game state: snake movement,
food, collision detection, and scoring.
"""


class Snake:
    def __init__(self, grid_size=20):
        self.grid_size = grid_size
        self.reset()

    def reset(self):
        """Reset snake to starting state."""
        center = self.grid_size // 2
        self.body = [
            (center,     center),
            (center - 1, center),
            (center - 2, center),
        ]
        self.direction  = (1, 0)   # moving right
        self.next_dir   = (1, 0)
        self.alive      = True
        self.score      = 0
        self.level      = 1

    def change_direction(self, new_dir):
        """Change direction — prevent reversing into itself."""
        opposite = (-new_dir[0], -new_dir[1])
        if opposite != self.direction:
            self.next_dir = new_dir

    def step(self, food_pos):
        """
        Move the snake one step forward.
        Returns True if food was eaten, False otherwise.
        """
        self.direction = self.next_dir
        head_x, head_y = self.body[0]
        dir_x,  dir_y  = self.direction

        new_head = (head_x + dir_x, head_y + dir_y)

        # Wall collision
        if not (0 <= new_head[0] < self.grid_size and
                0 <= new_head[1] < self.grid_size):
            self.alive = False
            return False

        # Self collision
        if new_head in self.body:
            self.alive = False
            return False

        self.body.insert(0, new_head)

        # Check if food eaten
        if new_head == food_pos:
            self.score += self.level * 10
            self.level   = self.score // 50 + 1
            return True
        else:
            self.body.pop()
            return False

    def get_head(self):
        return self.body[0]