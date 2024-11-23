import pygame as pg
import numpy as np



class Brain:
    def __init__(self, n, j):
        self.n, self.j = n, j
        self.weights = np.random.rand(n, j)
        self.biases = np.random.rand(j)

    def activate(self, inputs):
        return np.dot(inputs, self.weights) + self.biases


class Being:
    def __init__(self, x, y, init_grid):
        self.x, self.y = x, y        
        self.grid = init_grid
        self.block_grid = np.zeros((init_grid.shape[0], init_grid.shape[1]), dtype=object)
        
        total_inputs = 0
        total_outputs = 0
        
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j] != 0:
                    block_class = color_map[self.grid[i, j]]["block_class"]
                    block = block_class(i, j)
                    self.block_grid[i, j] = block
                    
                    # Count sensing areas (inputs)
                    if hasattr(block, 'sensing_area'):
                        total_inputs += block.sensing_area
                    
                    # Count activatable blocks (outputs)
                    if hasattr(block, 'isActivatable') and block.isActivatable:
                        total_outputs += 1
        
        # Create brain with calculated dimensions
        self.brain = Brain(total_inputs, total_outputs)



    def draw(self, grid):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j] != 0:
                    grid.draw_cell(self.x + i, self.y + j, color_map[self.grid[i, j]]["rgb"])

    def manual_activate(self, output_index, value=1.0):
        """Manually activate a specific output"""
        outputs = np.zeros(self.brain.j)
        if 0 <= output_index < self.brain.j:
            outputs[output_index] = value
            activatable_blocks = self.get_activatable_blocks()
            if output_index < len(activatable_blocks):
                block = activatable_blocks[output_index]
                block.update_being(self)
                return outputs
        return None

    def get_activatable_blocks(self):
        """Return a list of all activatable blocks"""
        activatable = []
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                block = self.block_grid[i, j]
                if block and hasattr(block, 'isActivatable') and block.isActivatable:
                    activatable.append(block)
        return activatable

class MoverBlock:
    def __init__(self, x, y, orientation=0):
        self.x, self.y = x, y
        self.orientation = orientation
        self.isActivatable = True

    def update_being(self, being):
        if self.orientation == 0:
            being.x += 1
        elif self.orientation == 1:
            being.y += 1
        elif self.orientation == 2:
            being.x -= 1
        elif self.orientation == 3:
            being.y -= 1

class ConsumerBlock:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.isActivatable = True

    def update_being(self, being):
        pass


class RotatorBlock:
    def __init__(self, x, y, orientation=0):
        self.x, self.y = x, y
        self.orientation = orientation
        self.isActivatable = True
    def update_being(self, being):
        pass

class ShieldBlock:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.isActivatable = True

    def update_being(self, being):
        pass

class NeutralBlock:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.isActivatable = False
    def update_being(self, being):
        pass

class EyeBlock:
    def __init__(self, x, y, orientation=0):
        self.x, self.y = x, y
        self.orientation = orientation
        self.sensing_area = 16
        self.isActivatable = False

    def update_being(self, being):
        pass


class ReproducerBlock:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.isActivatable = True

    def update_being(self, being):
        pass

class EarBlock:
    def __init__(self, x, y, orientation=0):
        self.x, self.y = x, y
        self.orientation = orientation
        self.sensing_area = 16
        self.isActivatable = False

    def update_being(self, being):
        pass

class CommunicatorBlock:
    def __init__(self, x, y, orientation=0):
        self.x, self.y = x, y
        self.orientation = orientation
        self.isActivatable = True

    def update_being(self, being):
        pass


color_map = {
    3: {
        "name": "mover",
        "color": "green",
        "rgb": (0, 255, 0),
        "block_class": MoverBlock
    },
    1: {
        "name": "consumer",
        "color": "red",
        "rgb": (255, 0, 0),
        "block_class": ConsumerBlock
    },
    4: {
        "name": "rotator",
        "color": "blue",
        "rgb": (0, 0, 255),
        "block_class": RotatorBlock
    },
    2: {
        "name": "eye",
        "color": "yellow",
        "rgb": (255, 255, 0),
        "block_class": EyeBlock
    },
}