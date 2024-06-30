from random import choice, randint
from pygame import Color, Vector2, gfxdraw, mouse, font
from .entity import Entity
from .camera import Camera

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

    def __init__(self, platform_size, name: str = "anon", *groups) -> None:
        super().__init__(*groups)

        self.can_eat = groups[0]

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
        self.font = font.Font("./assets/Ubuntu.ttf", 24)

    def eat(self, food: Entity, zoom):
        if not (
            Vector2(self.x, self.y).distance_to(Vector2(food.x, food.y))
            < self.radius - 3 / zoom
            and self.radius > food.radius
        ):
            return

        gaining_radius = 1
        gaining_score = 1

        if isinstance(food, Player):
            gaining_radius = food.radius * 0.75
            gaining_score = food.score / 2

        self.radius += gaining_radius
        self.score += gaining_score
        food.kill()

    def move(self, camera):
        mouse_pos = Vector2(mouse.get_pos())

        direction = Vector2(
            mouse_pos.x - camera.surface_width // 2, mouse_pos.y - camera.surface_height // 2
        )

        magnitude = sum([i**2 for i in direction.xy]) ** 0.5

        normal = Vector2(0, 0)

        if magnitude != 0:
            normal = direction / magnitude

        self.x += normal.x * self.speed
        self.y += normal.y * self.speed

    def update(self, camera: Camera) -> None:

        # move the player and checks if it can eat the foods or the players

        self.move(camera)

        for e in self.can_eat.sprites():
            can_draw, _ = e.can_draw(camera)

            if not can_draw:
                continue

            self.eat(e, camera.zoom)

    def draw(self, camera: Camera):

        # check if can draw player onto screen

        can_draw, center = self.can_draw(camera)

        if not can_draw: 
            return

        super().draw(camera)
        zoom = camera.zoom

        # draw player

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
        
        # draw player name

        text = self.font.render(self.name,False, "white")
        rect = text.get_rect()
        rect.center = (int(self.x * camera.zoom) + camera.rect.x, int(self.y * camera.zoom) + camera.rect.y)

        camera.surface.blit(text, rect)
