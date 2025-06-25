import pygame


pygame.init()
pygame.font.init()


WIDTH, HEIGHT = 1200, 800
FPS = 120
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLICKIE")
score = 0
new_score = 1
win_menu = "Start Screen"

CLICKER_MENU_CORDS = (WIDTH - 220, 0, 200, 100)
UPGRADE_MENU_CORDS = (WIDTH - 220, 100, 200, 100)
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
GREY = (128, 128, 128)
font = pygame.font.SysFont("comicsans", 60)


upgrades = {
    "upgrade1": {
        "name": "Upgrade 1",
        "cost": 10,
        "addition": 1,
        "effect": "Increases score gain by 1",
        "amount": 0
    },
    "upgrade2": {
        "name": "Upgrade 2",
        "cost": 100,
        "addition": 5,
        "effect": "Increases score gain by 5",
        "amount": 0
    },
    "upgrade3": {
        "name": "Upgrade 3",
        "cost": 1000,
        "addition": 50,
        "effect": "increase score gain by 50",
        "amount": 0
    },
}


def draw_clicker(mouse_pos, mouse_pressed):
    clicker_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 200)
    
    if clicker_rect.collidepoint(mouse_pos):
        if mouse_pressed:
            pygame.draw.rect(WIN, BLACK, clicker_rect)
            pygame.draw.rect(WIN, GREEN, clicker_rect.inflate(-20, -20))
        else:
            pygame.draw.rect(WIN, GREEN, clicker_rect)
    else:
        pygame.draw.rect(WIN, WHITE, clicker_rect)
    
    return clicker_rect

def draw_clicker_menu(mouse_pos, mouse_pressed):
    clicker_menu = pygame.draw.rect(WIN,GREY, CLICKER_MENU_CORDS)
    clicker_menu_rect = pygame.Rect(CLICKER_MENU_CORDS)

    if clicker_menu_rect.collidepoint(mouse_pos):
        if mouse_pressed:
            pygame.draw.rect(WIN, BLACK, clicker_menu_rect)
            pygame.draw.rect(WIN, GREEN, clicker_menu_rect.inflate(-20, -20))
        else:
            pygame.draw.rect(WIN, GREEN, clicker_menu_rect)

def draw_upgrade_menu(mouse_pos, mouse_pressed):
    upgrade_menu = pygame.draw.rect(WIN, GREY, UPGRADE_MENU_CORDS)
    upgrade_menu_rect = pygame.Rect(UPGRADE_MENU_CORDS)

    if upgrade_menu_rect.collidepoint(mouse_pos):
        if mouse_pressed:
            pygame.draw.rect(WIN, BLACK, upgrade_menu_rect)
            pygame.draw.rect(WIN, GREEN, upgrade_menu_rect.inflate(-20, -20))
        else:
            pygame.draw.rect(WIN, GREEN, upgrade_menu_rect)

    return upgrade_menu_rect


def draw_window(win_menu, mouse_pos, mouse_pressed):
    WIN.fill(BLACK)
    
    if win_menu == "Start Screen":
        start_text = font.render("Click to Start", True, WHITE)
        WIN.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))

    elif win_menu == "Game":
        topbar = pygame.draw.rect(WIN, GREY, (0, 0, WIDTH - 250, 100))
        score_text = font.render(f"Score: {score}", True, WHITE)
        WIN.blit(score_text, (0, 0))

        draw_clicker(mouse_pos, mouse_pressed)
        draw_clicker_menu(mouse_pos, mouse_pressed)
        draw_upgrade_menu(mouse_pos, mouse_pressed)

        
    elif win_menu == "Upgrade Menu":
        topbar = pygame.draw.rect(WIN, GREY, (0, 0, WIDTH - 250, 100))
        score_text = font.render(f"Score: {score}", True, WHITE)
        WIN.blit(score_text, (0, 0))

        draw_clicker_menu(mouse_pos, mouse_pressed)
        draw_upgrade_menu(mouse_pos, mouse_pressed)

    pygame.display.update()


def main(win_menu):
    global score
    Run = True
    Clock = pygame.time.Clock()
    clicked = False

    while Run:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        if win_menu == "Start Screen":
            if mouse_pressed and not clicked:
                win_menu = "Game"
                clicked = True
            elif not mouse_pressed:
                clicked = False
        
        elif win_menu == "Game":
            clicker_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 200)
            upgrade_menu_rect = pygame.Rect(UPGRADE_MENU_CORDS)
            if mouse_pressed and clicker_rect.collidepoint(mouse_pos) and not clicked:
                score += new_score
                clicked = True
            elif mouse_pressed and upgrade_menu_rect.collidepoint(mouse_pos) and not clicked:
                win_menu = "Upgrade Menu"
            elif not mouse_pressed:
                clicked = False
            
        elif win_menu == "Upgrade Menu":
            clicker_menu_rect = pygame.Rect(CLICKER_MENU_CORDS)
            if mouse_pressed and clicker_menu_rect.collidepoint(mouse_pos) and not clicked:
                win_menu = "Game"
                clicked = True
            elif not mouse_pressed:
                clicked = False

        draw_window(win_menu, mouse_pos, mouse_pressed)


if __name__ == "__main__":
    main(win_menu)

#redo of everything
#---------------------------------------------------------
# setup
#---------------------------------------------------------
import pygame
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1500, 1000
FPS = 120
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLICKIE")

Font_Size = 50
score = 0
new_score = 1
win_menu = "Start Screen"

CLICKER_MENU_CORDS = (WIDTH - 220, 0, 200, 100)
UPGRADE_MENU_CORDS = (WIDTH - 220, 110, 200, 100)
font = pygame.font.SysFont("comicsans", Font_Size)


#---------------------------------------------------------
#upgrades
#---------------------------------------------------------

class Upgrade:
    def __init__(self, name, cost, addition, effect):
        self.name = name
        self.cost = cost
        self.addition = addition
        self.effect = effect
        self.amount = 0

    def apply_upgrade(self):
        global new_score
        new_score += self.addition
        self.amount += 1

upgrade1 = Upgrade("Upgrade 1", 10, 1, "Increases score gain by 1")
upgrade2 = Upgrade("Upgrade 2", 100, 5, "Increases score gain by 5")
upgrade3 = Upgrade("Upgrade 3", 1000, 50, "Increases score gain by 50")

#---------------------------------------------------------
#clicker
#---------------------------------------------------------

class Clicker:
    def __init__(self,x ,y ,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_clicker(self):
        print("draw clicker")

#---------------------------------------------------------
#draw modules
#---------------------------------------------------------
def score_display():
    score_text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (0, 0))

def start_screen():
    WIN.fill("black")
    start_text = font.render("Click to Start", True, WHITE)
    WIN.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))
    pygame.display.update()

def clicker(mouse_pos, mouse_pressed, clicked):
    clicker_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 200)
    pygame.draw.rect(WIN, "white", clicker_rect)
    if clicker_rect.collidepoint(mouse_pos):
        if mouse_pressed and not clicked:
            pygame.draw.rect(WIN, "black", clicker_rect)
            pygame.draw.rect(WIN, "green", clicker_rect.inflate(-20, -20))
            return clicked == True  # Click detected
        else:
            pygame.draw.rect(WIN, "green", clicker_rect)
    else:
        pygame.draw.rect(WIN, "white", clicker_rect)
    return False  # No click



#---------------------------------------------------------
#script
#---------------------------------------------------------

def main():
    global score, new_score, win_menu
    RUN = True
    CLOCK = pygame.time.Clock()
    clicked = False

    while RUN:
        CLOCK.tick(FPS)
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False  # Reset click state on release

        WIN.fill("black")

        if win_menu == "Start Screen":
            start_screen()
            if mouse_pressed and not clicked:
                win_menu = "Game"
                clicked = True
        
        elif win_menu == "Game":
            # Check if clicker was clicked and update score
            if clicker(mouse_pos, mouse_pressed, clicked == True):
                score += new_score
            
            
            # Display score in game mode
            score_display()

        pygame.display.flip()
        
#---------------------------------------------------------
#run
#---------------------------------------------------------

if __name__ == "__main__":
    main()