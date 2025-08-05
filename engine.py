import pygame
from Constants import WIDTH, HEIGHT, FONT_SIZE

class Engine:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", FONT_SIZE)
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CLICKIE")

engine = Engine()