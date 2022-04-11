import pygame
from pygame.image import load


def load_img(filename: str):
    img = load(filename)
    img.convert()
    return img


def transform_img(img: pygame.Surface | str, size: tuple | float):
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
