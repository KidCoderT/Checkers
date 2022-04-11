import sys
import pygame
from utils import *

pygame.init()

width, height = 720, 720
DISPLAY = pygame.display.set_mode((width, height))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock()


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


while True:
    DISPLAY.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_board()

    pygame.display.update()
    clock.tick()
