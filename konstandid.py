import pygame
import os
import json

VEERUD = 10
READ = 20
BLOCK = 30
LAIUS = BLOCK * VEERUD
KÕRGUS = BLOCK * READ

FPS = 60
# VÄRVID
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
DARK_PURPLE = (48, 25, 52)
COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN]

# Tetromino kujud ja värvid
TETROMINOS = {
    "I": {"shape": [(0, 1), (0, 0), (0, -1), (0, -2)], "color": CYAN},
    "O": {"shape": [(0, 0), (0, 1), (1, 0), (1, 1)], "color": YELLOW},
    "T": {"shape": [(0, 0), (-1, 0), (1, 0), (0, -1)], "color": PURPLE},
    "S": {"shape": [(0, 0), (1, 0), (0, -1), (-1, -1)], "color": GREEN},
    "Z": {"shape": [(0, 0), (-1, 0), (0, -1), (1, -1)], "color": RED},
    "J": {"shape": [(0, -1), (0, 0), (0, 1), (-1, 1)], "color": BLUE},
    "L": {"shape": [(0, -1), (0, 0), (0, 1), (1, 1)], "color": ORANGE},
}
# 2x konstandid
flash_color = RED
last_flash_switch = pygame.time.get_ticks()
flash_interval = 500


# Laeb sätted settings.json failist
def load_settings():
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as f:
            data = json.load(f)
            if "skoor" not in data:  # workaround kui keegi kasutab vana settings faili
                data["skoor"] = list()
            return data
    else:
        # Kui faili pole, siis loob ise faili
        settings = {"veerud": VEERUD, "read": READ, "skoor:": list()}
        save_settings(settings)
        return settings


# salvestab sätted Json faili
def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f)
