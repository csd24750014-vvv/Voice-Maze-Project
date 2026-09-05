import pygame
import sys

# 1. Initialize Pygame engine
pygame.init()

# 2. Screen Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Voice Maze")

# Colors
BG_COLOR = (40, 44, 52)
PLAYER_COLOR = (0, 200, 100)  # Green

# Player Setup
player_size = 40
player_x = (WIDTH // 2) - (player_size // 2)
player_y = (HEIGHT // 2) - (player_size // 2)

# Frame Rate Controller
clock = pygame.time.Clock()
FPS = 60

# 3. Main Game Loop
def main():
    running = True
    
    while running:
        # A. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # B. Game Logic Updates (Movement will go here)

        # C. Rendering
        screen.fill(BG_COLOR)
        
        # Draw the player
        pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_size, player_size))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()