# Tetris screen size
VEERUD = 10
READ = 20
BLOCK = 30  # A single unit that makes up a block
LAIUS = BLOCK * VEERUD
KÕRGUS = BLOCK * READ

# Colors
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
COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN]

# Tetromino shapes and colors
TETROMINOS = {
    "I": {"shape": [(0, 1), (0, 0), (0, -1), (0, -2)], "color": CYAN},
    "O": {"shape": [(0, 0), (0, 1), (1, 0), (1, 1)], "color": YELLOW},
    "T": {"shape": [(0, 0), (-1, 0), (1, 0), (0, -1)], "color": PURPLE},
    "S": {"shape": [(0, 0), (1, 0), (0, -1), (-1, -1)], "color": GREEN},
    "Z": {"shape": [(0, 0), (-1, 0), (0, -1), (1, -1)], "color": RED},
    "J": {"shape": [(0, -1), (0, 0), (0, 1), (-1, 1)], "color": BLUE},
    "L": {"shape": [(0, -1), (0, 0), (0, 1), (1, 1)], "color": ORANGE},
}
