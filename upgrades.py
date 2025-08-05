import pygame
from engine import engine

class Upgrade:
    instances = []

    def __init__(self, name, cost, addition, effect, x, y, size_x, size_y):
        self.name = name
        self.cost = cost
        self.addition = addition
        self.effect = effect
        self.amount = 0
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        Upgrade.instances.append(self)  # Register instance for tracking
        # Animation properties
        self.click_animation_time = 0
        self.click_animation_duration = 10  # frames
        self.is_animating = False
        self.was_purchased = False  # Track successful purchases

    def apply_upgrade(self, game_state):
        game_state.new_score += self.addition
        self.amount += 1
    
    def can_afford(self, game_state):
        return game_state.score >= self.cost

    def purchase(self, game_state):
        if self.can_afford(game_state):
            game_state.score -= self.cost
            self.apply_upgrade(game_state)
            self.was_purchased = True  # Mark as purchased
            return True
        return False
    
    def draw(self, mouse_pos, mouse_pressed, clicked, game_state):
        upgrade_rect = pygame.Rect(self.x - self.size_x // 2, self.y - self.size_y // 2, self.size_x, self.size_y)
        
        # Animation logic
        if self.is_animating:
            # Draw animation based on purchase success
            if self.was_purchased:
                pygame.draw.rect(engine.win, "pink", upgrade_rect)
                shrink_factor = (self.click_animation_time / self.click_animation_duration)
                shrink_amount = int(20 * (1 - shrink_factor))
                pygame.draw.rect(engine.win, "green", upgrade_rect.inflate(-shrink_amount, -shrink_amount))
            else:
                pygame.draw.rect(engine.win, "pink", upgrade_rect)
                shrink_factor = (self.click_animation_time / self.click_animation_duration)
                shrink_amount = int(20 * (1 - shrink_factor))
                pygame.draw.rect(engine.win, "red", upgrade_rect.inflate(-shrink_amount, -shrink_amount))
            
            self.click_animation_time -= 1
            if self.click_animation_time <= 0:
                self.is_animating = False
                self.was_purchased = False
        else:
            base_color = "blue"
            if upgrade_rect.collidepoint(mouse_pos):
                base_color = "green"
            pygame.draw.rect(engine.win, base_color, upgrade_rect)

        # Text rendering (always on top)
        upgrade_text_name = engine.font.render(f"{self.name}", True, "white")
        upgrade_text_cost = engine.font.render(f"Cost: {self.cost:,}", True, "white")
        upgrade_text_effect = engine.font.render(f"Gain: {self.addition:,}", True, "white")

        engine.win.blit(upgrade_text_name, (self.x - 50, self.y + 15))
        engine.win.blit(upgrade_text_cost, (self.x - 50, self.y + 45))
        engine.win.blit(upgrade_text_effect, (self.x - 50, self.y + 75))

        # Handle clicks
        if upgrade_rect.collidepoint(mouse_pos) and mouse_pressed and not clicked:
            self.is_animating = True
            self.click_animation_time = self.click_animation_duration
            return self.purchase(game_state)
        return False
   
# upgrade - upgrade("name", cost, addition, effect, x, y, size_x, size_y)
upgrade1 = Upgrade("Upgrade 1", 10, 1, "Increases score gain by 1",100, 150, 100, 50)
upgrade2 = Upgrade("Upgrade 2", 100, 5, "Increases score gain by 5",100, 300, 100, 50)
upgrade3 = Upgrade("Upgrade 3", 1_000, 50, "Increases score gain by 50",100, 450, 100, 50)
upgrade4 = Upgrade("Upgrade 4", 10_000, 500, "Increases score gain by 500",100, 600, 100, 50)
upgrade5 = Upgrade("Upgrade 5", 1_000_000, 10000, "Increases score gain by 10,000",100, 750, 100, 50)
upgrade6 = Upgrade("Upgrade 6", 10_000_000, 100000, "Increases score gain by 100,000",100, 900, 100, 50)

class AutomaticUpgrade:
    instances = []

    def __init__(self, name, cost, addition, effect, x, y, size_x, size_y):
        self.name = name
        self.cost = cost
        self.addition = addition
        self.effect = effect
        self.amount = 0
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        AutomaticUpgrade.instances.append(self)  # Register instance for tracking
        # Animation properties
        self.click_animation_time = 0
        self.click_animation_duration = 10  # frames
        self.is_animating = False
        self.was_purchased = False  # Track successful purchases

    def apply_upgrade(self, game_state):
        game_state.automatic_score_gain += self.addition
        self.amount += 1
    
    def can_afford(self, game_state):
        return game_state.score >= self.cost

    def purchase(self, game_state):
        if self.can_afford(game_state):
            game_state.score -= self.cost
            self.apply_upgrade(game_state)
            self.was_purchased = True  # Mark as purchased
            return True
        return False
    
    def draw(self, mouse_pos, mouse_pressed, clicked, game_state):
        upgrade_rect = pygame.Rect(self.x - self.size_x // 2, self.y - self.size_y // 2, self.size_x, self.size_y)
        
        # Animation logic
        if self.is_animating:
            # Draw animation based on purchase success
            if self.was_purchased:
                pygame.draw.rect(engine.win, "pink", upgrade_rect)
                shrink_factor = (self.click_animation_time / self.click_animation_duration)
                shrink_amount = int(20 * (1 - shrink_factor))
                pygame.draw.rect(engine.win, "green", upgrade_rect.inflate(-shrink_amount, -shrink_amount))
            else:
                pygame.draw.rect(engine.win, "pink", upgrade_rect)
                shrink_factor = (self.click_animation_time / self.click_animation_duration)
                shrink_amount = int(20 * (1 - shrink_factor))
                pygame.draw.rect(engine.win, "red", upgrade_rect.inflate(-shrink_amount, -shrink_amount))
            
            self.click_animation_time -= 1
            if self.click_animation_time <= 0:
                self.is_animating = False
                self.was_purchased = False
        else:
            # Normal draengine.wing
            base_color = "blue"
            if upgrade_rect.collidepoint(mouse_pos):
                base_color = "green"
            pygame.draw.rect(engine.win, base_color, upgrade_rect)

        # Text rendering (always on top)
        upgrade_text_name = engine.font.render(f"{self.name}", True, "white")
        upgrade_text_cost = engine.font.render(f"Cost: {self.cost:,}", True, "white")
        upgrade_text_effect = engine.font.render(f"Gain: {self.addition:,} per second", True, "white")

        engine.win.blit(upgrade_text_name, (self.x - 50, self.y + 15))
        engine.win.blit(upgrade_text_cost, (self.x - 50, self.y + 45))
        engine.win.blit(upgrade_text_effect, (self.x - 50, self.y + 75))

        # Handle clicks
        if upgrade_rect.collidepoint(mouse_pos) and mouse_pressed and not clicked:
            self.is_animating = True
            self.click_animation_time = self.click_animation_duration
            return self.purchase(game_state)
        return False

automaticupgrade1 = AutomaticUpgrade("Auto Upgrade 1", 100, 1, "Increases score gain by 1 every second", 100, 150, 100, 50)
automaticupgrade2 = AutomaticUpgrade("Auto Upgrade 2", 1_000, 10, "Increases score gain by 5 every second", 100, 300, 100, 50)
automaticupgrade3 = AutomaticUpgrade("Auto Upgrade 3", 10_000, 75, "Increases score gain by 50 every second", 100, 450, 100, 50)