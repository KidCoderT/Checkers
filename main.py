import sys
import pygame
from utils import *
from constants import *

pygame.init()

from board import Board

DISPLAY = pygame.display.set_mode((width, height))
pygame.display.set_caption("Checkers")

images = {
    "red": [
        load_img("assets/red-checker/standard.png"),
        load_img("assets/red-checker/king.png"),
    ],
    "black": [
        load_img("assets/black-checker/standard.png"),
        load_img("assets/black-checker/king.png"),
    ],
}

debug_font = pygame.font.SysFont("fira code", 20)
DEBUG = False


def draw_board():
    for file in range(8):
        for rank in range(8):
            isLightSquare = (file + rank) % 2 == 0
            color = (244, 250, 255) if isLightSquare else (160, 179, 195)
            position = {"x": (width / 8) * file, "y": (height / 8) * rank}

            pygame.draw.rect(
                DISPLAY,
                color,
                pygame.Rect(position["x"], position["y"], width / 8, height / 8),
            )

            position = {
                "x": (width / 8) * file + cell_width / 2,
                "y": (height / 8) * rank + cell_height / 2,
            }

            # For Debugging
            if DEBUG:
                text = debug_font.render(str(8 * rank + file), False, (0, 0, 0))
                rect = text.get_rect(center=(position["x"], position["y"]))
                DISPLAY.blit(text, rect.topleft)


game = Board(images)

while True:
    DISPLAY.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            file, rank = mx // cell_width, my // cell_height
            index = int(file + rank * 8)

            game.active_piece = game.board[index]
            game.board[index] = None

        if event.type == pygame.MOUSEBUTTONUP:
            if game.active_piece is not None:
                file, rank = mx // cell_width, my // cell_height
                index = int(file + rank * 8)

                game.active_piece.reset_index(index)
                game.board[index] = game.active_piece
                game.active_piece = None

    draw_board()

    for piece in game.board:
        if piece is not None:
            piece.show(DISPLAY)

    if game.active_piece is not None:
        game.active_piece.show(DISPLAY, (mx, my))

    pygame.display.update()
    clock.tick()
