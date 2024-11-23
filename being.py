import pygame as pg
import numpy as np
from constants import color_map



class Brain:
    def __init__(self):
        pass


class Being:
    def __init__(self, x, y, init_grid):
        self.x, self.y = x, y        
        self.grid = init_grid
        self.block_grid = np.zeros((init_grid.shape[0], init_grid.shape[1]), dtype=object)
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j] != 0:
                    block_class = color_map[self.grid[i, j]]["block_class"]
                    self.block_grid[i, j] = block_class()

    def draw(self, grid):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j] != 0:
                    grid.draw_cell(i, j, color_map[self.grid[i, j]]["rgb"])
