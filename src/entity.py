from pygame import Surface
from pygame.sprite import Sprite
from .camera import Camera


class Entity(Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        self.image = Surface((0, 0))
        self.rect = self.image.get_rect()
        self.x, self.y = 0, 0
        self.radius = 0

    def draw(self, camera: Camera):
        pass

    def get_camera(self) -> Camera | None:
        for x in self.groups():
            if isinstance(x, Camera):
                return x

        return None
