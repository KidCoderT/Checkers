import pygame
from utils import load_img
from constants import *


class Piece:
    def __init__(self, images, color, index):
        self.index = index
        self.color = color
        self.type = 0
        self.my_images: dict = images[color]
        self.image: pygame.surface.Surface = self.my_images[self.type]
        self.setup()

    def setup(self):
        if self.color == "red":
            self.direction = "+"
        else:
            self.direction = "-"

    def show(self, surface):
        file, rank = self.index % 8, self.index // 8
        position = (
            (width / 8) * file + (cell_width / 2) - (self.image.get_width() * 0.58),
            (height / 8) * rank + (cell_height / 2) - (self.image.get_height() * 0.50),
        )
        surface.blit(self.image, position)


class Board:
    def __init__(self, images):
        self.images = images

        self.board: list[None | Piece] = [None for _ in range(64)]
        self.board[0] = Piece(self.images, "red", 0)
        self.board[5] = Piece(self.images, "black", 5)
        self.board[50] = Piece(self.images, "red", 50)
