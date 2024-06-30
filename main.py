import pygame
from src.camera import Camera
from src.grid import Grid
from src.player import Player
from src.food import Food
from src.hud import Hud
from src.bot import Bot

# Dimension Definitions
PLATFORM_SIZE = 1000

# Other Definitions
NAME = "agar.io"
VERSION = "0.2"

# Pygame initialization
pygame.init()
SCREEN = pygame.display.set_mode(flags=pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_width(), SCREEN.get_height()
pygame.display.set_caption("{} - v{}".format(NAME, VERSION))
pygame.display.set_icon(pygame.image.load("./assets/logo.png").convert_alpha())

cam = Camera(SCREEN_WIDTH,SCREEN_HEIGHT)
eatable = pygame.sprite.Group()

grid = Grid(pygame.Color(51,51,51),PLATFORM_SIZE,25,3,cam)

for _ in range(1000):
    Food(PLATFORM_SIZE, cam, eatable)

for _ in range(5):
    Bot(PLATFORM_SIZE,cam, eatable)

player = Player(PLATFORM_SIZE,"anon",cam, eatable)
hud = Hud(player,cam)
clock = pygame.time.Clock()

while(True):
    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
        if(e.type == pygame.QUIT):
            pygame.quit()
            quit()

    cam.surface.fill((22,22,22))
    cam.custom_draw()
    cam.update(player)

    SCREEN.blit(cam.surface, cam.surface.get_rect())
    
    pygame.display.flip()
    clock.tick(60)
