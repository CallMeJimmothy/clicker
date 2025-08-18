import pygame
from engine import engine
from Constants import WIDTH, HEIGHT

def score_display(game_state):
    score_text = engine.font.render(f"Score: {game_state.score:,}", True, "white")
    engine.win.blit(score_text, (0, 0))

def start_screen(win):
    win.fill("black")
    start_text = engine.font.render("Click to Start", True, "white")
    win.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 
                         HEIGHT // 2 - start_text.get_height() // 2))