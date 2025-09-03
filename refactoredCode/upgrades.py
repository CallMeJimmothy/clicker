import pygame
import math
from Constants import HEIGHT, WIDTH
from engine import engine
from gamestate import game_state

class Upgrades:
    upgrades_instances = []
    def __init__(self, name , x, y, width, height, power, cost, upgrade_type):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.power = power
        self.cost = cost
        self.upgrade_type = upgrade_type
        self.amount = 0
        self.font = pygame.font.SysFont("Arial", 20)
        Upgrades.upgrades_instances.append(self)

        # animation properties
        self.is_animating = False
        self.animation_duration = 20  # Duration of the animation in frames
        self.animation_time = 0

        #hover animation properties
        self.current_scale = 1.0
        self.target_scale = 1.0
        self.hover_animation_speed = 0.1

    def draw_upgrade(self, mouse_pos, mouse_pressed, clicked):
        # colours
        default_color = "white"
        hover_color = (46, 139, 87) # Dark Sea Green
        click_colour = (46, 139, 87) # Dark Sea Green
        text_color = "white"
        upgrade_text = self.font.render(f"{self.name} (Cost: {self.cost}) | (addition: {self.power})", True, text_color)

        # scale factors
        hover_scale_factor = 1.1
        min_scale_factor = 0.9  # How small it gets when shrinking
        max_scale_factor = 1.15

        # Update hover target scale based on mouse position
        self.target_scale = hover_scale_factor if self.rect.collidepoint(mouse_pos) else 1.0

        # Smoothly interpolate current scale towards target scale
        self.current_scale += (self.target_scale - self.current_scale) * self.hover_animation_speed

        # Handle click
        if mouse_pressed and self.rect.collidepoint(mouse_pos) and not clicked:
            pygame.draw.rect(engine.win, click_colour, self.rect)
            self.is_animating = True
            self.animation_time = self.animation_duration
            return True
        
        # Handle animation
        if self.is_animating:
            # Calculate the animation progress (0 to 1)
            progress = self.animation_time / self.animation_duration

            # Create a bouncing effect using sine wave
            bounce_factor = min_scale_factor + (1 + math.sin(progress * math.pi * 2)) * (max_scale_factor - min_scale_factor) / 2

            # Draw the bouncing rectangle
            current_width = int(self.rect.width * bounce_factor)
            current_height = int(self.rect.height * bounce_factor)
            current_x = self.rect.centerx - current_width // 2
            current_y = self.rect.centery - current_height // 2
            animated_rect = pygame.Rect(current_x, current_y, current_width, current_height)
            pygame.draw.rect(engine.win, click_colour, animated_rect)

            # Decrement animation timer
            self.animation_time -= 1

            # End animation when timer reaches 0
            if self.animation_time <= 0:
                self.is_animating = False
                self.animation_time = 0
        # Handle hover effect (when not animating)
        elif not self.is_animating:
            current_width = int(self.rect.width * self.current_scale)
            current_height = int(self.rect.height * self.current_scale)
            current_x = self.rect.centerx - current_width // 2
            current_y = self.rect.centery - current_height // 2
            hover_rect = pygame.Rect(current_x, current_y, current_width, current_height)
            color = hover_color if self.rect.collidepoint(mouse_pos) else default_color
            pygame.draw.rect(engine.win, color, hover_rect)
            engine.win.blit(upgrade_text, (hover_rect.x, hover_rect.y + 50))
        
        return False
    
    def purchase_upgrade(self):
        if game_state.score >= self.cost:
            game_state.score -= self.cost
            self.amount += 1
            if self.upgrade_type == "click":
                game_state.new_score += self.power
            if self.upgrade_type == "auto":
                game_state.automatic_score_gain += self.power

#upgrades
upgrade1 = Upgrades("Upgrade 1", 30, 150, 250, 50, power=1, cost=10, upgrade_type="click")
upgrade2 = Upgrades("Upgrade 2", 30, 250, 250, 50, power=5, cost=50, upgrade_type="click")
