import pygame
import sys
from core.maze_logic import build_walls

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Voice Maze - MVP Foundation")

# Colors
BG_COLOR = (40, 44, 52)
PLAYER_COLOR = (0, 200, 100)
WALL_COLOR = (200, 50, 50)
GOAL_COLOR = (255, 215, 0) # Gold
TEXT_COLOR = (255, 255, 255)

# Game Setup
player_size = 40
player_speed = 5
walls = build_walls()

# Goal coordinates (bottom right of our specific maze layout)
goal_rect = pygame.Rect(18 * 40, 12 * 40, 40, 40) 

# Font Setup
title_font = pygame.font.Font(None, 74)
inst_font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
FPS = 60

def reset_player():
    return pygame.Rect(40, 40, player_size, player_size)

def main():
    player_rect = reset_player()
    game_state = "MENU" # Can be: "MENU", "PLAYING", "VICTORY"
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # State Transitions via Keyboard
            if event.type == pygame.KEYDOWN:
                if game_state == "MENU" and event.key == pygame.K_RETURN:
                    game_state = "PLAYING"
                elif game_state == "VICTORY" and event.key == pygame.K_r:
                    player_rect = reset_player()
                    game_state = "MENU"

        screen.fill(BG_COLOR)

        if game_state == "MENU":
            # Draw Menu Screen
            title_surf = title_font.render("VOICE MAZE", True, TEXT_COLOR)
            inst_surf = inst_font.render("Press ENTER to Start", True, TEXT_COLOR)
            screen.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, HEIGHT//3))
            screen.blit(inst_surf, (WIDTH//2 - inst_surf.get_width()//2, HEIGHT//2))

        elif game_state == "PLAYING":
            # Draw Active Game
            keys = pygame.key.get_pressed()
            old_x, old_y = player_rect.x, player_rect.y

            if keys[pygame.K_LEFT]: player_rect.x -= player_speed
            if keys[pygame.K_RIGHT]: player_rect.x += player_speed
            if keys[pygame.K_UP]: player_rect.y -= player_speed
            if keys[pygame.K_DOWN]: player_rect.y += player_speed

            # Wall Collisions
            for wall in walls:
                if player_rect.colliderect(wall):
                    player_rect.x, player_rect.y = old_x, old_y

            # Victory Check
            if player_rect.colliderect(goal_rect):
                game_state = "VICTORY"

            for wall in walls:
                pygame.draw.rect(screen, WALL_COLOR, wall)
            pygame.draw.rect(screen, GOAL_COLOR, goal_rect)
            pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

        elif game_state == "VICTORY":
            # Draw Victory Screen
            win_surf = title_font.render("LEVEL COMPLETE", True, GOAL_COLOR)
            reset_surf = inst_font.render("Press 'R' to Return to Menu", True, TEXT_COLOR)
            screen.blit(win_surf, (WIDTH//2 - win_surf.get_width()//2, HEIGHT//3))
            screen.blit(reset_surf, (WIDTH//2 - reset_surf.get_width()//2, HEIGHT//2))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()