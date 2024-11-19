class Block:
    def __init__(self):
        pass

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), (self.x, self.y, 10, 10))

