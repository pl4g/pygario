from random import choice, randint
from pygame import Color, Vector2, gfxdraw, mouse
from .entity import Entity
from .camera import Camera
from . import utils


class Player(Entity):
    COLORS = [
        Color(37, 7, 255),
        Color(35, 183, 253),
        Color(48, 254, 241),
        Color(19, 79, 251),
        Color(255, 7, 230),
        Color(255, 7, 23),
        Color(6, 254, 13),
    ]

    def __init__(self, platform_size,name: str = "anon", *groups) -> None:
        super().__init__(*groups)

        self.can_eat = groups[1]

        self.x = randint(-platform_size, platform_size)
        self.y = randint(-platform_size, platform_size)

        self.score = 0

        self.speed = 1.5
        self.radius = 15
        self.color: Color = choice(self.COLORS)
        self.out_color = Color(
            int(self.color.r * 2 / 3),
            int(self.color.g * 2 / 3),
            int(self.color.b * 2 / 3),
        )
        self.name = name

    def eat(self, food: Entity, zoom):
        if not (utils.get_distance(Vector2(self.x, self.y), Vector2(food.x, food.y)) < self.radius - 3 / zoom and self.radius > food.radius):
            return

        gaining_radius = 1
        gaining_score = 1

        if isinstance(food, Player):
            gaining_radius = food.radius * 0.75
            gaining_score = food.score / 2

        self.radius += gaining_radius
        self.score += gaining_score
        food.kill()

    def move(self):
        mouse_pos = Vector2(mouse.get_pos())

        _, SCREEN_WIDTH, SCREEN_HEIGHT = utils.get_screen()

        direction = Vector2(
            mouse_pos.x - SCREEN_WIDTH // 2, mouse_pos.y - SCREEN_HEIGHT // 2
        )
        magnitude = sum([i**2 for i in direction.xy]) ** 0.5

        normal = Vector2(0, 0)

        if magnitude != 0:
            normal = direction / magnitude

        self.x += normal.x * self.speed
        self.y += normal.y * self.speed

    def update(self) -> None:
        self.move()

        cam = self.get_camera()
        if cam is None:
            return

        for e in cam.sprites():
            if e in self.can_eat.sprites():
                self.eat(e, cam.zoom)

    def draw(self, camera: Camera):
        super().draw(camera)

        zoom = camera.zoom
        x, y = camera.x, camera.y

        center = Vector2(int(self.x * zoom + x), int(self.y * zoom + y))

        # Draw the ouline of the player as a darker, bigger circle
        gfxdraw.aacircle(
            camera.surface,
            int(center.x),
            int(center.y),
            int((self.radius / 2 + 3 / zoom) * zoom),
            self.out_color,
        )

        gfxdraw.filled_circle(
            camera.surface,
            int(center.x),
            int(center.y),
            int((self.radius + 3 / zoom) * zoom),
            self.out_color,
        )

        gfxdraw.filled_circle(
            camera.surface,
            int(center.x),
            int(center.y),
            int(self.radius * zoom),
            self.color,
        )
