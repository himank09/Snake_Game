import pygame
from snake_game import Snake
from food import Food

# --- Configuration & Colors ---
CELL_SIZE = 25  # How many pixels wide/tall each grid square is
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self, grid_size=20):
        # Your existing logic setup
        self.grid_size = grid_size
        self.snake = Snake(grid_size)
        self.food = Food(grid_size)
        self.food.place(self.snake.body)
        self.running = True

        # --- Pygame Setup ---
        pygame.init()
        # The window size is the grid size multiplied by the pixel size of each cell
        window_size = self.grid_size * CELL_SIZE 
        self.screen = pygame.display.set_mode((window_size, window_size))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

    def update(self):
        """Advance the game by one step."""
        if not self.snake.alive:
            self.running = False
            return

        ate = self.snake.step(self.food.position)
        if ate:
            self.food.place(self.snake.body)

    def restart(self):
        """Reset everything for a new game."""
        self.snake.reset()
        self.food.place(self.snake.body)
        self.running = True

    def draw(self):
        """"Renders the game state to the screen."""
        self.screen.fill(BLACK) # Clear the screen

        # Draw the food
        fx, fy = self.food.position
        pygame.draw.rect(self.screen, RED, (fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw the snake
        for (x, y) in self.snake.body:
            pygame.draw.rect(self.screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # --- NEW: Draw the Score ---
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.snake.score}", True, (255, 255, 255)) # White text
        self.screen.blit(score_text, (10, 10)) # Draw it at coordinates (10, 10)

        pygame.display.flip() # Swap the display buffers to show what we drew   
        
    def run(self):
        """The main game loop."""
        # Setup a font for the Game Over text
        font = pygame.font.Font(None, 30)

        while True:
            # 1. Event Handling (Keys, Quitting)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return # Exit the loop and close the game
                
                if event.type == pygame.KEYDOWN:
                    # --- NEW: Restart Game ---
                    if event.key == pygame.K_r and not self.running:
                        self.restart()

                    # --- NEW: Use your built-in change_direction method! ---
                    if self.running:
                        if event.key == pygame.K_UP:
                            self.snake.change_direction((0, -1))
                        elif event.key == pygame.K_DOWN:
                            self.snake.change_direction((0, 1))
                        elif event.key == pygame.K_LEFT:
                            self.snake.change_direction((-1, 0))
                        elif event.key == pygame.K_RIGHT:
                            self.snake.change_direction((1, 0))

            # 2. Update Game State
            if self.running:
                self.update()

            # 3. Render Graphics
            self.draw()

            # --- NEW: Game Over Screen ---
            if not self.running:
                text = font.render("GAME OVER! Press 'R' to Restart", True, (255, 255, 255))
                # Center the text on the screen
                text_rect = text.get_rect(center=(self.grid_size * CELL_SIZE // 2, self.grid_size * CELL_SIZE // 2))
                self.screen.blit(text, text_rect)
                pygame.display.flip() # Update the screen to show the text

            # 4. Control Speed (FPS)
            # Starts at 10 FPS, and gets faster as your level increases!
            current_speed = 10 + ((self.snake.level - 1) * 2)
            self.clock.tick(current_speed)

# To actually start the game when you run this file:
if __name__ == "__main__":
    game = Game()
    game.run()