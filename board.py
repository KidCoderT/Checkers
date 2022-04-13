import pygame
from utils import load_img
from constants import *

black_start = [1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23]
red_start = [40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62]


class Move:
    def __init__(self, index, is_promotion=False, to_kill=None):
        self.index = index
        self.is_promotion = is_promotion
        self.to_kill = to_kill


class Piece:
    def __init__(self, images, color, index, direction):
        self.index = index
        self.color = color
        self.type = 0
        self.my_images: dict = images[color]
        self.image: pygame.surface.Surface = self.my_images[self.type]
        self.possible_moves: list[Move] = []

        self.direction = direction
        self.is_king = False

    def reset_index(self, index):
        self.index = index

    def show(self, surface, pos=None):
        if pos is None:
            file, rank = self.index % 8, self.index // 8
            position = (
                (width / 8) * file + (cell_width / 2) - (self.image.get_width() * 0.58),
                (height / 8) * rank
                + (cell_height / 2)
                - (self.image.get_height() * 0.50),
            )
            surface.blit(self.image, position)
        else:
            position = (
                pos[0] - (self.image.get_width() * 0.58),
                pos[1] - (self.image.get_height() * 0.50),
            )
            surface.blit(self.image, position)

    """
     0  1  2  3  4  5  6  7
     8  9 10 11 12 13 14 15
    16 17 18 19 20 21 22 23
    24 25 26 27 28 29 30 31

    top right -7
    top left -9
    bottom left 7
    bottom right 9

    + means go down
    - means go up
    """

    def find_possible_moves(self, board):
        self.possible_moves = []
        if self.is_king:
            index_offsets = [-7, -9, 9, 7]
        else:
            index_offsets = [-7, -9] if self.direction == "-" else [9, 7]

        for offset in index_offsets:
            new_index = self.index + offset
            to_kill = None
            is_promotion = False

            for i in range(2):
                if board[new_index] is None:
                    is_promotion = 0 <= new_index <= 7 or 56 <= new_index <= 63
                    if i == 1:
                        to_kill = new_index - offset

                    self.possible_moves.append(Move(new_index, is_promotion, to_kill))
                    break
                elif board[new_index].color == self.color:
                    break
                new_index += offset

    def promote(self):
        self.is_king = True
        self.type = 1
        self.image = self.my_images[self.type]
        self.direction = "+-"


class Board:
    def __init__(self, images):
        self.images = images

        self.board: list[None | Piece] = [None for _ in range(64)]
        self.active_piece: None | Piece = None

        self.arrange_board()

    def arrange_board(self):
        for index in black_start:
            self.board[index] = Piece(self.images, "black", index, "+")
        for index in red_start:
            self.board[index] = Piece(self.images, "red", index, "-")
