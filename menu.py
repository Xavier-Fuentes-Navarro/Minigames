import pygame
import math


d1=1280
d2=720
pygame.init()
screen = pygame.display.set_mode((d1, d2))
clock = pygame.time.Clock()



# ASCII art del título "MINIJUEGO"
ASCII_TITLE = [
"$$\\      $$\\ $$$$$$\\ $$\\   $$\\ $$$$$$\\   $$$$$\\ $$\\   $$\\ $$$$$$$$\\  $$$$$$\\   $$$$$$\\   $$$$$$\\  ",
"$$$\\    $$$ |\\_$$  _|$$$\\  $$ |\\_$$  _|  \\__$$ |$$ |  $$ |$$  _____|$$  __$$\\ $$  __$$\\ $$  __$$\\ ",
"$$$$\\  $$$$ |  $$ |  $$$$\\ $$ |  $$ |       $$ |$$ |  $$ |$$ |      $$ /  \\__|$$ /  $$ |$$ /  \\__|",
"$$\\$$\\$$ $$ |  $$ |  $$ $$\\$$ |  $$ |       $$ |$$ |  $$ |$$$$$\\    $$ |$$$$\\ $$ |  $$ |\\$$$$$$\\  ",
"$$ \\$$$  $$ |  $$ |  $$ \\$$$$ |  $$ | $$\\   $$ |$$ |  $$ |$$  __|   $$ |\\_$$ |$$ |  $$ | \\____$$\\ ",
"$$ |\\$  /$$ |  $$ |  $$ |\\$$$ |  $$ | $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$\\   $$ |",
"$$ | \\_/ $$ |$$$$$$\\ $$ | \\$$ |$$$$$$\\\\$$$$$$  |\\$$$$$$  |$$$$$$$$\\ \\$$$$$$  | $$$$$$  |\\$$$$$$  |",
"\\__|     \\__|\\______|\\__|  \\__|\\______|\\______/  \\______/ \\________| \\______/  \\______/  \\______/ "
]



FONT = pygame.font.SysFont("Courier", 18, bold=False)

def draw_ascii_vertical_wave(ascii_lines, t):
    base_x = 125   # Posición horizontal fija
    base_y = d2//3  # Posición inicial del bloque ASCII

    for i, line in enumerate(ascii_lines):

        # Onda vertical (sube y baja)
        vertical_offset = int(math.sin(t + i * 0.3) * 10)

        y = base_y + i * 22 + vertical_offset
        x = base_x

        text_surface = FONT.render(line, True, (0, 255, 120))
        screen.blit(text_surface, (x, y))


t = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 20))

    draw_ascii_vertical_wave(ASCII_TITLE, t)

    pygame.display.flip()
    t += 0.05
    clock.tick(60)

pygame.quit()