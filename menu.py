from main import*
def load_settings():  #Hetkel on eraldi json fail veerude ja ridade muutmiseks, hiljem saab lisada sätte kiiruse muutmiseks jne
    with open('settings.json', 'r') as f:
        return json.load(f)

def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def draw_button(screen, button_text, center_x, center_y, action=None): #Funktsioon nuppude joonistamiseks
    font = pygame.font.Font(None, 36)
    text = font.render(button_text, True, WHITE)
    text_rect = text.get_rect(center=(center_x, center_y))

    button_rect = text_rect.inflate(20, 10)
    pygame.draw.rect(screen, WHITE, button_rect, 2)

    screen.blit(text, text_rect)
    return button_rect

def run_menu(): #menüü
    pygame.init()
    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption("Tetris")

    menu_running = True
    while menu_running:
        screen.blit(pygame.image.load("menüü.png"), (0,0)) #Menüü taustapilt

        # nupud
        play_button = draw_button(screen, 'MÄNGI', 150, 200)
        settings_button = draw_button(screen, 'Sätted', 150, 300)

        for event in pygame.event.get(): #Nupuvajutuse kontroll
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    main()
                elif settings_button.collidepoint(pygame.mouse.get_pos()):
                    run_settings_menu()

        pygame.display.flip()

def run_settings_menu(): #Sätete menüü
    settings = load_settings()
    screen = pygame.display.get_surface()
    settings_running = True

    while settings_running:
        screen.fill(BLACK)
        read_button = draw_button(screen, f'Read: {settings["read"]}', 150, 250)
        read_button_increase = draw_button(screen, "+", 65, 250)
        read_button_decrease = draw_button(screen, "-", 235, 250)

        veerud_button = draw_button(screen, f'Veerud: {settings["veerud"]}', 150, 300)
        veerud_button_increase = draw_button(screen, "+", 55, 300)
        veerud_button_decrease = draw_button(screen, "-", 240, 300)

        Default_button = draw_button(screen, "Default", 150, 350)

        for event in pygame.event.get(): #Kontrollib, kas ja mis nuppu vajutati, ja reageerib vastavalt
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                if read_button_increase.collidepoint(mouse_pos):
                    settings["read"] += 5  # suurendab vajutusega ridasi 5 võrra
                    if settings["read"] > 30:  # Max ridade arv on 30
                        settings["read"] = 10  # Kui läheb üle 30 siis loopib tagasi algusesse
                if read_button_decrease.collidepoint(mouse_pos):
                    settings["read"] -= 5
                    if settings["read"] < 10:
                        settings["read"] = 10
                elif veerud_button_increase.collidepoint(mouse_pos):
                    settings["veerud"] += 5
                    if settings["veerud"] > 30:
                        settings["veerud"] = 5
                elif veerud_button_decrease.collidepoint(mouse_pos):
                    settings["veerud"] -= 5
                    if settings["veerud"] < 5:
                        settings["veerud"] = 5
                elif Default_button.collidepoint(mouse_pos):
                    settings["veerud"] = 10
                    settings["read"] = 20
            back_button = draw_button(screen, 'Tagasi', 150, 450)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    settings_running=False
                    pygame.display.update()

    save_settings(settings)
    pygame.display.flip()



if __name__ == "__main__":
    run_menu()