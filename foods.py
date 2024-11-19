class Food:
    def __init__(self):
        self.x, self.y = 0, 0

    def draw(self, screen):
        pg.draw.circle(screen, (0, 255, 0), (self.x, self.y), 5)
