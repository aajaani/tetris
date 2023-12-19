import pygame
from konstandid import *


class Tetromino:  # Loob tetrise ja kontrollib operatsioone tetrise blokkidega
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        for coord in self.shape:
            pygame.draw.rect(
                screen,
                self.color,
                (self.x + coord[0] * BLOCK, self.y + coord[1] * BLOCK, BLOCK, BLOCK),
            )  # loob tetrise bloki

    def move(self, dx, dy):  # funktsioon liikumiseks
        self.x += dx
        self.y += dy

    def rotate(self):  # funktsioon bloki pööramiseks
        self.shape = [(y, -x) for x, y in self.shape]

    def get_rotate_kuju(
        self,
    ):  # funktsioon, mis tagastab bloki pööratud asukoha koordinaadid, et kontrollida, kas saab pöörata
        return [(y, -x) for x, y in self.shape]
