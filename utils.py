import pygame
from pygame.image import load
from constants import cell_width, cell_height


def load_img(filename: str):
    img = load(filename)
    img = transform_img(img, (cell_width * 0.7, cell_height * 0.7))
    img.convert()
    return img


def transform_img(img: pygame.surface.Surface | str, size: tuple | float):
    if isinstance(size, float):
        n_img = load_img(img)  # type: ignore
        new_w = n_img.get_width() * size
        new_h = n_img.get_height() * size
        n_img = pygame.transform.scale(n_img, (new_w, new_h))
        n_img.convert()
        return n_img

    n_img = pygame.transform.scale(img, size)  # type: ignore
    n_img.convert()
    return n_img
