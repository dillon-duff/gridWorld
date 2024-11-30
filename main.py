import pygame as pg
import numpy as np
from constants import WIDTH, HEIGHT
from being import Being
import random

class Grid:
    def __init__(self, width, height, cell_size):
        self.cell_size = cell_size
        self.cols = width // cell_size
        self.rows = height // cell_size
        self.width = self.cols * cell_size
        self.height = self.rows * cell_size
        self.screen = pg.display.set_mode((self.width, self.height))
        
    def draw_cell(self, row, col, color):
        """Draw a colored square at grid position (row, col)"""
        pg.draw.rect(self.screen, color,
                    (col * self.cell_size, 
                     row * self.cell_size,
                     self.cell_size,
                     self.cell_size))
    
    def get_cell_from_pos(self, x, y):
        """Convert screen coordinates to grid coordinates"""
        col = x // self.cell_size
        row = y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return row, col
        return None

    def fill(self, color):
        """Fill entire screen with color"""
        self.screen.fill(color)

pg.init()

grid = Grid(WIDTH, HEIGHT, 5)
clock = pg.time.Clock()

being_grid = np.zeros((5, 5))

# being_grid[0, 1] = 1
# being_grid[0, 2] = 1
# being_grid[0, 3] = 1

# being_grid[1, 0] = 1
# being_grid[2, 0] = 1
# being_grid[3, 0] = 1

# being_grid[1, 4] = 1
# being_grid[2, 4] = 1
# being_grid[3, 4] = 1

being_grid[4, 1] = 1
being_grid[4, 2] = 1
being_grid[4, 3] = 1

being_grid[1, 1] = 2
being_grid[1, 2] = 4
being_grid[1, 3] = 2

being_grid[2, 1] = 3
being_grid[2, 2] = 4
being_grid[2, 3] = 3

being_grid[3, 1] = 2
being_grid[3, 2] = 3
being_grid[3, 3] = 2

def generate_random_square_grid(size, max_value):
    grid = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            grid[i, j] = np.random.randint(0, max_value + 1)
    return grid


beings = [Being(100, 100, being_grid)] + [Being(random.randint(0, grid.cols), random.randint(0, grid.rows), generate_random_square_grid(5, 4)) for _ in range(10)]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            cell = grid.get_cell_from_pos(*mouse_pos)
            if cell:
                row, col = cell

                print(row, col)

    keys = pg.key.get_pressed()
    for being in beings:
        # Number keys 1-9 will activate different outputs
        for i in range(9):
            if keys[pg.K_1 + i]:
                outputs = being.manual_activate(i)
                if outputs is not None:
                    activatable_blocks = being.get_activatable_blocks()
                    print(f"Activated output {i}, affecting {len(activatable_blocks)} blocks")
                    print(f"Block type was {activatable_blocks[i]}")
        being.update()

    grid.fill((0, 0, 0))

    for being in beings:
        being.draw(grid)

    pg.display.flip()
    clock.tick(60)
