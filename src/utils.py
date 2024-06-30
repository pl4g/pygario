import pygame

def get_screen():
    screen = pygame.display.get_surface()

    return screen, screen.get_width(),screen.get_height()

def get_distance(a: pygame.Vector2, b: pygame.Vector2):
    return a.distance_to(b)
