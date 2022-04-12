import pygame
from utils import load_img
from constants import *

black_start = [1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23]
red_start = [40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62]


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
        self.arrange_board()

    def arrange_board(self):
        for index in black_start:
            self.board[index] = Piece(self.images, "black", index)
        for index in red_start:
            self.board[index] = Piece(self.images, "red", index)
