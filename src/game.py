import pygame
from src.camera import Camera
from src.grid import Grid
from src.player import Player
from src.food import Food
from src.hud import Hud
from src.bot import Bot


class Game:
    def __init__(
        self,
        screen: pygame.Surface,
        player_name: str = "anon",
        platform_size: int = 500,
        bots: int = 3,
    ) -> None:



        eatable = pygame.sprite.Group()

        player = Player(platform_size, player_name, eatable)

        self.cam = Camera(screen, player, Grid(pygame.Color(51, 51, 51), platform_size, 50, 3), Hud(player))
        self.cam.add([Bot(platform_size, eatable) for _ in range(bots)], [Food(platform_size, eatable) for _ in range(1000)])
        self.cam.sort()

        self.clock = pygame.time.Clock()
        pass

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    running = False

            self.cam.update()
            self.cam.custom_draw()

            self.clock.tick(60)
        pass
