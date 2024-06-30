from pygame import Surface, SRCALPHA
from pygame.sprite import Group


class Camera(Group):
    def __init__(self, width, height) -> None:
        super().__init__()

        self.surface = Surface((width, height), SRCALPHA)

        self.x, self.y = 0, 0
        self.width, self.height = width, height

        self.zoom = 0.5

    def center(self, pos: tuple):
        x, y = pos
        self.x = -x * self.zoom + (self.width / 2)
        self.y = -y * self.zoom + (self.height / 2)

    def update(self, player) -> None:
        self.zoom = 100 / player.radius + 0.3
        self.center((player.x, player.y))
        return super().update()

    def custom_draw(self):
        for e in self.sprites():
            e.draw(self)
