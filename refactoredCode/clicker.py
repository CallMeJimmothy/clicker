import pygame
import math
from engine import engine
from Constants import HEIGHT, WIDTH

class Clicker:
    click_animation_duration = 20
    hover_animation_speed = 0.1

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        
        self.is_animating = False
        self.click_animation_time = 0
        self.current_scale = 1.0
        self.target_scale = 1.0
        
    def draw_clicker(self, mouse_pos, mouse_pressed, clicked):
        default_color = "white"
        hover_color = (46, 139, 87)
        click_colour = (46, 139, 87)
        
        hover_scale_factor = 1.2
        min_scale_factor = 0.8
        max_scale_factor = 1.3
        
        clicker_circle = pygame.Rect(self.x - self.width, self.y - self.width, self.width * 2, self.width * 2)
        
        self.target_scale = hover_scale_factor if clicker_circle.collidepoint(mouse_pos) else 1.0
        self.current_scale += (self.target_scale - self.current_scale) * self.hover_animation_speed
        
        if mouse_pressed and clicker_circle.collidepoint(mouse_pos) and not clicked:
            self.is_animating = True
            self.click_animation_time = self.click_animation_duration
            return True
        
        if self.is_animating:
            progress = self.click_animation_time / self.click_animation_duration
            bounce_factor = min_scale_factor + (1 + math.sin(progress * math.pi * 2)) * (max_scale_factor - min_scale_factor) / 2
            current_width = int(self.width * bounce_factor)
            pygame.draw.circle(engine.win, click_colour, (self.x, self.y), current_width)
            self.click_animation_time -= 1
            
            if self.click_animation_time <= 0:
                self.is_animating = False
                self.click_animation_time = 0
        
        elif not self.is_animating:
            current_width = int(self.width * self.current_scale)
            color = hover_color if clicker_circle.collidepoint(mouse_pos) else default_color
            pygame.draw.circle(engine.win, color, (self.x, self.y), current_width)
        
        return False