from .entity import Entity
from .camera import Camera
from random import randint, choice
from pygame import Color, Vector2, gfxdraw

class Food(Entity):
    COLORS = [
        Color(80,252,54),
        Color(36,244,255),
        Color(243,31,46),
        Color(4,39,243),
        Color(254,6,178),
        Color(255,211,7),
        Color(216,6,254),
        Color(145,255,7),
        Color(7,255,182),
        Color(255,6,86),
        Color(147,7,255)
    ]
    
    def __init__(self,platform_size, *groups):
        super().__init__(*groups)

        platform_size -= 20

        self.x = randint(-platform_size,platform_size)
        self.y = randint(-platform_size,platform_size)

        self.radius = 7
        self.color = choice(self.COLORS)

    def draw(self, camera: Camera):
        zoom = camera.zoom
        x,y = camera.x, camera.y

        center = Vector2(int(self.x*zoom + x), int(self.y*zoom + y))
        gfxdraw.filled_circle(camera.surface, int(center.x),int(center.y), int(self.radius*zoom), self.color)
