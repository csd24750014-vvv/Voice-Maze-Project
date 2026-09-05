import pygame

# X = Wall, Space = Path
MAZE_LAYOUT = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X X       X        X",
    "X X XXXXX X XXXXXX X",
    "X X X   X X X    X X",
    "X   X X X   X XX X X",
    "XXXXX X XXXXX XX X X",
    "X     X          X X",
    "X XXXXXXXXXXXXXXXX X",
    "X X              X X",
    "X X XXXXXXXXXXXX X X",
    "X X X          X X X",
    "X X X XXXXXXXX X X X",
    "X X X          X   X",
    "X X XXXXXXXXXXXXXX X",
    "XXXXXXXXXXXXXXXXXXXX"
]

def build_walls():
    walls = []
    for row_idx, row in enumerate(MAZE_LAYOUT):
        for col_idx, tile in enumerate(row):
            if tile == "X":
                # Multiply by 40px to get screen coordinates
                walls.append(pygame.Rect(col_idx * 40, row_idx * 40, 40, 40))
    return walls