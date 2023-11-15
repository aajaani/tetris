import random
import pygame
class TetrisSkooritabel:
    def __init__(self):
        self.skoor = 0
        self.multiplier_active = False
        self.multiplier_end_time = None

    def activate_multiplier(self):
        self.multiplier_active = True
        self.multiplier_end_time = pygame.time.get_ticks() + 5000  # 5 sekundit

    def check_multiplier_timeout(self):
        if self.multiplier_active and pygame.time.get_ticks() > self.multiplier_end_time:
            self.multiplier_active = False

    def kustuta_read(self, kustutatud_read):
        if self.multiplier_active:
            self.skoor += (kustutatud_read * 50) * 2  # Multiplied skoor
        else:
            self.skoor += kustutatud_read * 50

        if kustutatud_read == 3:
            self.skoor += 100 if not self.multiplier_active else 200
        elif kustutatud_read == 4:
            self.skoor += 250 if not self.multiplier_active else 500

    def saa_skoor(self):
        return self.skoor



