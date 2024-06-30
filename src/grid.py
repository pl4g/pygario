import pygame
from .entity import Entity
from .camera import Camera


class Grid(Entity):
    """Used to represent the backgroun grid."""

    def __init__(self,color: pygame.Color = pygame.Color(51,51,51), size:int = 10000, delta_size: int = 25, thickness: int = 3, *groups):
        super().__init__(*groups)

        self.color = color
        self.size = size
        self.tile_size = delta_size 
        self.thickness = thickness

    def draw(self, camera: Camera):
        # A grid is a set of horizontal and prependicular lines
        zoom = camera.zoom
        x, y = camera.x, camera.y

        for i in range(-self.size, self.size, self.tile_size):
            pygame.draw.line(
                camera.surface,
                self.color,
                (x - self.size * zoom, i * zoom + y),
                (self.size * zoom + x, i * zoom + y),
                self.thickness,
            )

            pygame.draw.line(
                camera.surface,
                self.color,
                (i * zoom + x, y - self.size * zoom),
                (i * zoom + x, self.size * zoom + y),
                self.thickness,
            )
