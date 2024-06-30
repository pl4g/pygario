from pygame import Surface, Vector2
from pygame.sprite import Sprite
from .camera import Camera


class Entity(Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        self.image = Surface((0, 0))
        self.rect = self.image.get_rect()
        self.x, self.y = 0, 0
        self.radius = 0

    def can_draw(self, camera:Camera) -> tuple[bool,Vector2]:
        zoom = camera.zoom
        x, y = camera.rect.x, camera.rect.y

        center = Vector2(int(self.x * zoom + x), int(self.y * zoom + y))

        if center.x > camera.surface_width + (self.radius * 3) or center.x < - self.radius * 3:
            return False, center

        if center.y > camera.surface_height + (self.radius * 3) or center.y < - self.radius * 3:
            return False, center

        return True, center

    def draw(self, camera: Camera):
        pass

    def get_camera(self) -> Camera | None:
        for x in self.groups():
            if isinstance(x, Camera):
                return x

        return None
