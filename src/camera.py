import pygame
from pygame.sprite import Group


class Camera(Group):
    def __init__(self, screen, player, grid, hud):
        super().__init__()

        self.surface = screen
        self.surface_width = screen.get_width()
        self.surface_height = screen.get_height()
        self.rect = self.surface.get_rect()

        self.player = player
        self.grid = grid
        self.hud = hud

        self.add(player, grid, hud)

        self.zoom = 0.5

    def center(self):
        if self.player is None:
            return

        self.rect.centerx = -self.player.x * self.zoom + (self.rect.width)
        self.rect.centery = -self.player.y * self.zoom + (self.rect.height)

    def sort(self):
        # sort the list

        order = ["Grid", "Food", "Bot", "Hud", "Player"]
        ordered = sorted(
            self.sprites(), key=lambda spr: order.index(type(spr).__name__)
        )

        self.empty()
        self.add(ordered)

    def update(self):
        new_zoom = 100 / self.player.radius + 0.3

        if new_zoom != self.zoom:
            self.zoom = new_zoom

        self.center()
        return super().update(self)

    def custom_draw(self):
        self.surface.fill((22, 22, 22))

        self.grid.draw(self)

        for entity in self.sprites():
            if entity.can_draw(self)[0]:
                entity.draw(self)

        self.hud.draw(self)

        self.surface.blit(self.surface, self.surface.get_rect())
        pygame.display.flip()
