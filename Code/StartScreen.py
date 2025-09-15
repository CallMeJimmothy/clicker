import pygame
from gamestate import game_state
from engine import engine
from Constants import WIDTH, HEIGHT

def start_screen():
    if game_state.win_menu == "start screen":
        engine.win.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 48)
        text_surface = font.render("Click to Start", True, "white")
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        engine.win.blit(text_surface, text_rect)

        if game_state.mouse_pressed and not game_state.clicked:
            game_state.clicked = True
            game_state.win_menu = "clicker"