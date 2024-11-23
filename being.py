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

    def draw(self, grid):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j] != 0:
                    grid.draw_cell(i, j, color_map[self.grid[i, j]]["rgb"])
