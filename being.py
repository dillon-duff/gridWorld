# Contains colors/cell types and coordinates based on the relative 0,0 being the top left corner of the 'being'

# Contains a neural network brain that receives inputs and outputs actions

# Energy can be consumed and is consumed proportional to size, brain size/usage, and actions

# Can interact with other beings

# Can consume food to gain energy

# Can reproduce with another being

# Cell types (colors)
# Green: Move forward
# Red: Consume
# Blue: Rotate
# Gray: Do nothing
# Brown: Shield
# Yellow: Sensor? Eye? Vision cone?
# Purple: Reproduce

import pygame as pg

class Being:
    grid = []
    def __init__(self):
        self.x, self.y = 0, 0

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), (self.x, self.y), 10)

