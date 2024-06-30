import argparse
import sys
import pygame
from src.game import Game

# Pygame initialization
parser = argparse.ArgumentParser(
    "pygar.io", description="An agar.io clone made in python with pygame."
)

parser.add_argument("player_name", default="anon", type=str, help="The player name")
parser.add_argument("bots", default=3, type=int, help="The number of bots")

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

if not any(vars(args).values()):
    parser.print_help()
    parser.exit()

if not args.__contains__("help"):
    pygame.init()
    SCREEN = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    pygame.display.set_caption("pygar.io")
    pygame.display.set_icon(pygame.image.load("./assets/logo.png").convert_alpha())

    game = Game(SCREEN, args.player_name, 1000, args.bots)
    game.main()

pygame.quit()
