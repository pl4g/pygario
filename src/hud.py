from pygame import Color, Surface, font
from .entity import Entity
from .camera import Camera
from .player import Player


class Hud(Entity):
    def __init__(self, player: Player, *groups) -> None:
        super().__init__(*groups)

        self.scoreboard = Surface((95, 25))

        self.scoreboard_width = self.scoreboard.get_width()
        self.scoreboard_height = self.scoreboard.get_height()

        self.scoreboard.fill((50, 50, 50, 70))

        self.font = font.Font("./assets/Ubuntu.ttf", 24)
        self.player = player

    def render_text(
        self,
        surf: Surface,
        message: str,
        color: Color | str,
        pos: tuple,
    ):

        text = self.font.render(message, True, color)
        rect = text.get_rect()
        rect.center = pos

        surf.blit(text, rect)

    def draw(self, camera: Camera):
        screen_height = camera.surface.get_height()

        self.render_text(
            self.scoreboard,
            str(int(self.player.score)),
            "white",
            (self.scoreboard_width // 2, self.scoreboard_height // 2),
        )

        camera.surface.blit(self.scoreboard, (5, screen_height - 30))

        self.scoreboard = Surface((95, 25))
        self.scoreboard.fill((50, 50, 50, 70))
