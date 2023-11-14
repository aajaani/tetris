import random

class TetrisSkooritabel:
    def __init__(self):
        self.skoor = 0
        self.kustutatud_read = 0

    def kustuta_read(self, kustutatud_read):
        self.skoor += kustutatud_read * 50

        for i in range(1, kustutatud_read):
            self.skoor += 5

        if kustutatud_read == 3:
            self.skoor += 100
        elif kustutatud_read == 4:
            self.skoor += 250

        if random.randint(1, 100) == 1:
            self.skoor += 1000

        self.kustutatud_read += kustutatud_read

    def saa_skoor(self):
        return self.skoor

