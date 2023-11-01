from main import*
from konstandid import*

class Tetromino: #loob tetrise plokke
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y
    def draw(self, screen):
        for coord in self.shape:
            pygame.draw.rect(screen, self.color, (self.x + coord[0]*BLOCK, self.y + coord[1]*BLOCK, BLOCK, BLOCK))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape=[(y, -x) for x, y in self.shape]

    def get_rotate_kuju(self):
        return [(y, -x) for x, y in self.shape]

