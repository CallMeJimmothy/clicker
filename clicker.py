import pygame


pygame.init()
pygame.font.init()

#Fun fact, the reason hysteria is often associated with women is because in the time of the ancient Greeks, it was believed to be caused by the uterus

Width, Height = 1200, 800
FPS = 120
WIN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("CLICKIE")
score = 0
new_score = 0
win_menu = "Start Screen"

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
GREY = (128, 128, 128)
font = pygame.font.SysFont("comicsans", 60)

upgrades = {
    "upgrade1": {
        "name": "Upgrade 1",
        "cost": 10,
        "addition": 1,
        "effect": "Increases score gain by 1"
    },
    "upgrade2": {
        "name": "Upgrade 2",
        "cost": 100,
        "addition": 5,
        "effect": "Increases score gain by 5"
    },
}

def draw_clicker(mouse_pos, mouse_pressed):
    clicker_rect = pygame.Rect(Width // 2 - 100, Height // 2 - 100, 200, 200)
    
    if clicker_rect.collidepoint(mouse_pos):
        if mouse_pressed:
            pygame.draw.rect(WIN, BLACK, clicker_rect)
            pygame.draw.rect(WIN, GREEN, clicker_rect.inflate(-20, -20))
        else:
            pygame.draw.rect(WIN, GREEN, clicker_rect)
    else:
        pygame.draw.rect(WIN, WHITE, clicker_rect)
    
    return clicker_rect

def draw_window(win_menu, mouse_pos, mouse_pressed):
    WIN.fill(BLACK)
    
    if win_menu == "Start Screen":
        start_text = font.render("Click to Start", True, WHITE)
        WIN.blit(start_text, (Width // 2 - start_text.get_width() // 2, 
                            Height // 2 - start_text.get_height() // 2))
    elif win_menu == "Game":
        # Draw score background and text
        pygame.draw.rect(WIN, GREY, (0, 0, 300, 100))
        score_text = font.render(f"Score: {score}", True, WHITE)
        WIN.blit(score_text, (0, 0))
        
        # Draw the clicker
        draw_clicker(mouse_pos, mouse_pressed)

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
            # Add click detection and score increment
            clicker_rect = pygame.Rect(Width // 2 - 100, Height // 2 - 100, 200, 200)
            if mouse_pressed and clicker_rect.collidepoint(mouse_pos) and not clicked:
                score += 1
                clicked = True
            elif not mouse_pressed:
                clicked = False
            
        draw_window(win_menu, mouse_pos, mouse_pressed)

if __name__ == "__main__":
    main(win_menu)