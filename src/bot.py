from random import choice, random, uniform
from .player import Player
from pygame import Color, Vector2


class Bot(Player):
    COLORS = [
        Color(37, 7, 255),
        Color(35, 183, 253),
        Color(48, 254, 241),
        Color(19, 79, 251),
        Color(255, 7, 230),
        Color(255, 7, 23),
        Color(6, 254, 13),
    ]

    """
    Shout out to soupgang and other mofos for the names
    """

    NAMES = [
        "soupboyplague",
        "socks",
        "socaquigrandão",
        "helenobrian",
        "neukgames",
        "boglots",
        "cachogames",
        "kangaceiroz",
        "bnzgepeto",
        "cachorro1337",
        "etherealharmonies",
        "SaturnCSS",
    ]

    def __init__(self, platform_size, *groups) -> None:
        super().__init__(platform_size, choice(self.NAMES), *groups)

        self.direction = Vector2(uniform(-1, 1), uniform(-1, 1))

    def move(self, camera):
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed

    def update(self, camera) -> None:
        if random() < 0.02:
            self.direction = Vector2(uniform(-1, 1), uniform(-1, 1))

        super().update(camera)
