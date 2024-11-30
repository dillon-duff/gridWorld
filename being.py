import pygame as pg
import numpy as np



class Brain:
    def __init__(self, n, j):
        self.n, self.j = n, j
        self.weights = np.random.uniform(-1, 1, (n, j))
        self.biases = np.random.uniform(-1, 1, j)

    def activate(self, inputs):
        z = np.dot(inputs, self.weights) + self.biases
        return 1 / (1 + np.exp(-z))


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

                    # TODO: Add orientation to blocks based on genome
                    
                    # Count sensing areas (inputs)
                    if hasattr(block, 'sensing_length'):
                        total_inputs += block.sensing_length ** 2
                    
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
    
    def update(self):
        inputs = self.get_inputs()
        outputs = self.brain.activate(inputs)
        print(outputs)
        self.apply_outputs(outputs)

    def get_inputs(self):
        inputs = []
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                block = self.block_grid[i, j]
                if block and hasattr(block, 'sensing_length'):
                    inputs.append(block.get_sense_data(self, self.grid))

        return [inp for sublist in inputs for inp in sublist]

    def apply_outputs(self, outputs):
        activatable_blocks = self.get_activatable_blocks()
        for i, output in enumerate(outputs):
            if i < len(activatable_blocks):
                block = activatable_blocks[i]
                if output > 0.5:  # Activation threshold, maybe make this a parameter?
                    block.update_being(self)

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
        # Check if all blocks in the 3x3 grid surrounding the RotatorBlock have non-zero values
        all_nonzero = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Check if coordinates are within grid bounds
                if (0 <= self.x + i < being.grid.shape[0] and 
                    0 <= self.y + j < being.grid.shape[1]):
                    if being.grid[self.x + i, self.y + j] == 0:
                        all_nonzero = False
                        break
                else:
                    all_nonzero = False
                    break
            if not all_nonzero:
                break

        if all_nonzero:
            # Get valid slice ranges within grid bounds
            x_start = max(0, self.x - 1)
            x_end = min(being.grid.shape[0], self.x + 2)
            y_start = max(0, self.y - 1) 
            y_end = min(being.grid.shape[1], self.y + 2)

            # Rotate the valid portion of the 3x3 grid
            rotated_grid = np.rot90(being.grid[x_start:x_end, y_start:y_end], 1)
            being.grid[x_start:x_end, y_start:y_end] = rotated_grid

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
        self.orientation = orientation  # 0: top-left, 1: top-right, 2: bottom-right, 3: bottom-left
        self.sensing_length = 4
        self.isActivatable = False

    def update_being(self, being):
        pass

    def get_sense_data(self, being, grid):
        # - Eye (sensor)
        # - Sees a square of blocks, where the eye is one of the square's corners
        sense_data = []
        
        # Determine scan ranges based on orientation
        if self.orientation == 0:  # Top-left corner
            x_range = range(self.x, self.x + self.sensing_length)
            y_range = range(self.y, self.y + self.sensing_length)
        elif self.orientation == 1:  # Top-right corner
            x_range = range(self.x, self.x + self.sensing_length)
            y_range = range(self.y, self.y - self.sensing_length, -1)
        elif self.orientation == 2:  # Bottom-right corner
            x_range = range(self.x, self.x - self.sensing_length, -1)
            y_range = range(self.y, self.y - self.sensing_length, -1)
        else:  # Bottom-left corner (orientation == 3)
            x_range = range(self.x, self.x - self.sensing_length, -1)
            y_range = range(self.y, self.y + self.sensing_length)
            
        # Scan the square area from the corner
        for i in x_range:
            for j in y_range:
                if 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]:
                    sense_data.append(grid[i, j])
                else:
                    sense_data.append(-99)  # Out of bounds value

        return sense_data


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
        self.sensing_length = 16
        self.isActivatable = False

    def update_being(self, being):
        pass

    def get_sense_data(self, being, grid):
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