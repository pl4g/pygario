from pygame import Color, Surface, font
from .entity import Entity
from .camera import Camera
from .player import Player, utils


class Hud(Entity):
    def __init__(self, player: Player, *groups) -> None:
        super().__init__(*groups)

        self.scoreboard = Surface((95, 25))
        self.scoreboard.fill((50, 50, 50, 70))
        self.font = font.Font("./assets/Ubuntu.ttf", 24)
        self.bold_font = font.Font("./assets/Ubuntu-bold.ttf", 24)
        self.player = player

    def render_text(
        self,
        surf: Surface,
        message: str,
        color: Color | str,
        pos: tuple,
        aa: bool = False,
        bold: bool = False,
    ):
        fnt = self.bold_font if bold else self.font

        text = fnt.render(message, aa, color)
        rect = text.get_rect()
        rect.center = pos

        surf.blit(text, rect)

    def draw(self, camera: Camera):
        _, _, screen_height = utils.get_screen()

        self.render_text(
            self.scoreboard,
            str(int(self.player.score)),
            "white",
            (self.scoreboard.get_width() // 2, self.scoreboard.get_height() // 2),
        )
        camera.surface.blit(self.scoreboard, (5, screen_height - 30))

        self.scoreboard = Surface((95, 25))
        self.scoreboard.fill((50, 50, 50, 70))

        for e in camera.sprites():
            if not hasattr(e,"name"):
                continue

            self.render_text(
                camera.surface,
                e.name,
                "white",
                (
                    e.x * camera.zoom + camera.x,
                    e.y * camera.zoom + camera.y,
                ),
            )
