import pygame
import sys
import json
from konstandid import BLOCK, LAIUS, KÕRGUS, WHITE, BLACK
from main import*
def load_settings():
    with open('settings.json', 'r') as f:
        return json.load(f)

def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def draw_button(screen, button_text, center_x, center_y, action=None):
    font = pygame.font.Font(None, 36)
    text = font.render(button_text, True, WHITE)
    text_rect = text.get_rect(center=(center_x, center_y))

    button_rect = text_rect.inflate(20, 10)
    pygame.draw.rect(screen, WHITE, button_rect, 2)

    screen.blit(text, text_rect)
    return button_rect

def run_menu():
    pygame.init()
    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption("Tetris Menu")

    menu_running = True
    while menu_running:
        screen.fill(BLACK)

        # Draw buttons
        play_button = draw_button(screen, 'MÄNGI', 150, 250)
        settings_button = draw_button(screen, 'Sätted', 150, 350)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    main()
                elif settings_button.collidepoint(pygame.mouse.get_pos()):
                    run_settings_menu()

        pygame.display.flip()

def run_settings_menu():
    settings = load_settings()
    screen = pygame.display.get_surface()
    settings_running = True

    while settings_running:
        screen.fill(BLACK)
        rows_button = draw_button(screen, f'Read: {settings["rows"]}', 150, 250)
        columns_button = draw_button(screen, f'Veerud: {settings["columns"]}', 150, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rows_button.collidepoint(pygame.mouse.get_pos()):
                    settings["rows"] += 5  # Increase rows by 5 for each click
                    if settings["rows"] > 25:  # Maximum rows set to 30
                        settings["rows"] = 5  # Loop back to minimum rows
                    save_settings(settings)
                elif columns_button.collidepoint(pygame.mouse.get_pos()):
                    settings["columns"] += 5  # Increase columns by 5 for each click
                    if settings["columns"] > 30:  # Maximum columns set to 30
                        settings["columns"] = 5  # Loop back to minimum columns
                    save_settings(settings)
                back_button = draw_button(screen, 'Tagasi', 150, 450)
                pygame.display.update()
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    settings_running=False
    pygame.display.flip()



if __name__ == "__main__":
    run_menu()