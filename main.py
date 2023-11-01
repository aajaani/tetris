import pygame
import sys
from pygame.locals import*
import random
from klassid import*
from konstandid import*

# Bloki liikumine alla timer
move_wait = 350
move_down_time = 100

screen = pygame.display.set_mode((LAIUS, KÕRGUS))

def grid(): #joonistab grid
    for x in range(0, LAIUS, BLOCK):
        pygame.draw.line(screen, GREY, (x, 0), (x, KÕRGUS), 1)
    for y in range(0, KÕRGUS, BLOCK):
        pygame.draw.line(screen, GREY, (0, y), (LAIUS, y), 1)

def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    move_time = pygame.time.get_ticks()
    current_tetromino = Tetromino(TETROMINOS["I"]["shape"], TETROMINOS["I"]["color"], LAIUS // 2, BLOCK * 2) #loob tetromino klassist objekti
    landed_data = [] #hoiab arvet, mis blokid juba kukkunud

    def check_collision(shape, dx, dy): #blokkidevaheline collision
        for coord in shape:
            x = (current_tetromino.x + coord[0] * BLOCK + dx) // BLOCK
            y = (current_tetromino.y + coord[1] * BLOCK + dy) // BLOCK
            if (x, y) in [block_coord for block_coord, _ in landed_data]:
                return True
            if x < 0 or x >= VEERUD or y >= READ:
                return True
        return False

    def clear_rows(): #puhastab read
        nonlocal landed_data
        for y in range(READ):
            if all((x, y) in [coord for coord, _ in landed_data] for x in range(VEERUD)):
                landed_data = [(coord, color) for coord, color in landed_data if coord[1] != y]
                for i, (coord, color) in enumerate(landed_data):
                    if coord[1] < y:
                        landed_data[i] = ((coord[0], coord[1] + 1), color)

    def landed_tetromino(): #peab arvet maandunud blokkie üle
        for coord in current_tetromino.shape:
            x = (current_tetromino.x + coord[0] * BLOCK) // BLOCK
            y = (current_tetromino.y + coord[1] * BLOCK) // BLOCK
            landed_data.append(((x, y), current_tetromino.color))
        clear_rows() #kui rida täis siis puhastab

    def spawn_tetromino():
        tetromino_nimi = random.choice("IOTSZJL")
        shape = TETROMINOS[tetromino_nimi]["shape"]
        color = TETROMINOS[tetromino_nimi]["color"]
        return Tetromino(shape, color, LAIUS // 2 - BLOCK * 2, 0)

    while True:
        screen.fill(BLACK)
        current_time = pygame.time.get_ticks()
        if current_time - move_time > move_wait: #blokk liigub alla kui kindel ajavahemik läbitud
            if not check_collision(current_tetromino.shape, 0, BLOCK):
                current_tetromino.move(0, BLOCK)
                move_time = current_time
            else: #kui ei saa alla liikuda enam, siis spawnib uue
                landed_tetromino()
                current_tetromino = spawn_tetromino()
                if check_collision(current_tetromino.shape, 0, 0):#kõpetab mängu kui blokid jõuab lakke
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #vasakule liikumine
                if event.key == pygame.K_LEFT and not check_collision(current_tetromino.shape, -BLOCK, 0):
                    current_tetromino.move(-BLOCK, 0)
                #paremale liikumine
                elif event.key == pygame.K_RIGHT and not check_collision(current_tetromino.shape, BLOCK, 0):
                    current_tetromino.move(BLOCK, 0)
                #pööramine
                elif event.key == pygame.K_SPACE:
                    rotated_shape = current_tetromino.get_rotate_kuju()
                    if not check_collision(rotated_shape, 0, 0):
                        current_tetromino.rotate()
        #kiiresti alla liikumine
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if current_time - move_time > move_down_time:
                if not check_collision(current_tetromino.shape, 0, BLOCK):
                    current_tetromino.move(0, BLOCK)gi
                    move_time = current_time
                else:
                    landed_tetromino()
                    current_tetromino = spawn_tetromino()

        grid()
        current_tetromino.draw(screen) #joonistab hetkese bloki ekraanile
        for (x, y), color in landed_data: #joonistab maandunud blokid ekraanile
            pygame.draw.rect(screen, color, (x * BLOCK, y * BLOCK, BLOCK, BLOCK))
        pygame.display.update()

if __name__ == "__main__":
    main()
