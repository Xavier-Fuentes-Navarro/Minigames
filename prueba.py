import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Estado del juego
current_game = "menu"
timer = 0
score = 0

# ------------------- MINIJUEGO 1: CORRE Y ESQUIVA -------------------
player = pygame.Rect(100, 300, 40, 40)
obstacles = []

# ------------------- MINIJUEGO 2: MEMORIA -------------------
sequence = []
player_input = []
colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]

# ------------------- MINIJUEGO 3: TOCA EL COLOR -------------------
target_color_index = 0
color_buttons = []

# ------------------- MINIJUEGO 4: TIEMPO PERFECTO -------------------
bar_x = 0
direction = 1

# ------------------- MINIJUEGO 5: ROMPECAJAS -------------------
falling_boxes = []

# ------------------- MINIJUEGO 6: ENCUENTRA AL IMPOSTOR -------------------
impostor_index = 0
objects = []

# ------------------- MINIJUEGO 7: PESCA -------------------
fishing_bar = 300
fish_spot = 350

# ------------------- MINIJUEGO 8: DIBUJA EL SÍMBOLO -------------------
pattern = []
drawing = []

# ------------------- MINIJUEGO 9: RECOGER MONEDAS -------------------
coins = []
player2 = pygame.Rect(400,300,40,40)

# ------------------- MINIJUEGO 10: DESARMA LA BOMBA -------------------
instructions = []
current_step = 0

# ------------------- FUNCIONES -------------------
def draw_text(text, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (20, y))

def reset_all():
    global player, obstacles, sequence, player_input, timer, score
    global falling_boxes, target_color_index, objects, impostor_index
    global bar_x, direction, coins, instructions, current_step

    player.x, player.y = 100, 300
    obstacles.clear()
    sequence.clear()
    player_input.clear()
    falling_boxes.clear()
    coins.clear()
    instructions.clear()
    pattern.clear()
    drawing.clear()
    timer = 0
    score = 0

# ------------------- MENU -------------------
def game_menu():
    screen.fill((10, 10, 30))
    draw_text("MINIJUEGOS (1-10)", 50)
    for i in range(1,11):
        draw_text(f"{i} - Juego {i}", 100 + i*30)
    draw_text("ESC - Salir", 550)

# ------------------- MINIJUEGO 1 -------------------
def game_runner():
    global timer, score
    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (0,200,200), player)
    timer += 1
    if timer % 40 == 0:
        obstacles.append(pygame.Rect(800, random.randint(0,560), 40, 40))
    for obs in obstacles:
        obs.x -= 6
        pygame.draw.rect(screen, (200,0,0), obs)
        if obs.colliderect(player): return "menu"
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.y -= 5
    if keys[pygame.K_s]: player.y += 5
    score += 1
    draw_text(f"Puntos: {score}", 20)
    return "game1"

# ------------------- MINIJUEGO 2 -------------------
def game_memory():
    global sequence, player_input, timer
    screen.fill((0, 0, 0))
    if len(sequence) == 0:
        sequence = [random.randint(0,3) for _ in range(4)]
        timer = 0
    if timer < 200:
        index = (timer // 50) % len(sequence)
        pygame.draw.rect(screen, colors[sequence[index]], pygame.Rect(300,200,200,200))
    else:
        for i,c in enumerate(colors):
            pygame.draw.rect(screen, c, pygame.Rect(150 + i*120, 450, 80, 80))
    if len(player_input) == len(sequence):
        if player_input == sequence: sequence.clear(); player_input.clear()
        else: return "menu"
    timer += 1
    return "game2"

# ------------------- MINIJUEGO 3 -------------------
def game_touch_color():
    global target_color_index
    screen.fill((0,0,0))
    if not color_buttons:
        for i,c in enumerate(colors): color_buttons.append(pygame.Rect(100+i*150,300,100,100))
        target_color_index = random.randint(0,3)
    draw_text(f"Toca el color correcto", 50)
    draw_text(f"Objetivo: {['ROJO','VERDE','AZUL','AMARILLO'][target_color_index]}", 100)
    for i,rect in enumerate(color_buttons): pygame.draw.rect(screen, colors[i], rect)
    return "game3"

# ------------------- MINIJUEGO 4 -------------------
def game_timing():
    global bar_x, direction
    screen.fill((0,0,0))
    bar_x += 7 * direction
    if bar_x <= 100 or bar_x >= 600: direction *= -1
    pygame.draw.rect(screen,(255,255,255),(100,250,600,50))
    pygame.draw.rect(screen,(0,255,0),(350,250,100,50))
    pygame.draw.rect(screen,(255,0,0),(bar_x,250,50,50))
    draw_text("Pulsa ESPACIO en la zona verde", 50)
    return "game4"

# ------------------- MINIJUEGO 5 -------------------
def game_break_boxes():
    global falling_boxes, score
    screen.fill((0,0,0))
    if random.random() < 0.05:
        falling_boxes.append(pygame.Rect(random.randint(0,760), 0, 40, 40))
    for b in falling_boxes[:]:
        b.y += 5
        pygame.draw.rect(screen,(200,200,0),b)
        if b.y > 600: return "menu"
    draw_text(f"Golpea las cajas (click)", 20)
    return "game5"

# ------------------- MINIJUEGO 6 -------------------
def game_impostor():
    global objects, impostor_index
    screen.fill((0,0,0))
    if not objects:
        impostor_index = random.randint(0,8)
        for i in range(9): objects.append(pygame.Rect(100+(i%3)*200,150+(i//3)*150,60,60))
    for i,obj in enumerate(objects):
        color = (0,255,0) if i!=impostor_index else (0,200,255)
        pygame.draw.rect(screen,color,obj)
    draw_text("Encuentra al impostor", 50)
    return "game6"

# ------------------- MINIJUEGO 7 -------------------
def game_fishing():
    global fishing_bar
    screen.fill((0,0,0))
    fishing_bar += random.randint(-5,5)
    fishing_bar = max(200,min(400,fishing_bar))
    pygame.draw.rect(screen,(255,255,255),(300,200,50,250))
    pygame.draw.rect(screen,(0,255,0),(300,fishing_bar,50,30))
    pygame.draw.rect(screen,(255,0,0),(300,fish_spot,50,20))
    draw_text("Alinea la barra verde con el pez", 50)
    return "game7"

# ------------------- MINIJUEGO 8 -------------------
def game_draw():
    global pattern
    screen.fill((0,0,0))
    if not pattern:
        for _ in range(5): pattern.append((random.randint(100,700),random.randint(100,500)))
    for p in pattern: pygame.draw.circle(screen,(255,0,0),p,10)
    for d in drawing: pygame.draw.circle(screen,(0,255,0),d,10)
    draw_text("Dibuja la forma", 20)
    return "game8"

# ------------------- MINIJuego 9 -------------------
def game_coins():
    global coins, score
    screen.fill((0,0,0))
    if random.random() < 0.03:
        coins.append(pygame.Rect(random.randint(0,760),random.randint(0,560),30,30))
    pygame.draw.rect(screen,(0,200,255),player2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: player2.y -= 5
    if keys[pygame.K_DOWN]: player2.y += 5
    if keys[pygame.K_LEFT]: player2.x -= 5
    if keys[pygame.K_RIGHT]: player2.x += 5
    for c in coins[:]:
        pygame.draw.rect(screen,(255,255,0),c)
        if player2.colliderect(c): coins.remove(c); score+=1
    draw_text(f"Monedas: {score}", 20)
    return "game9"

# ------------------- MINIJUEGO 10 -------------------
def game_bomb():
    global instructions, current_step
    screen.fill((0,0,0))
    if not instructions:
        instructions = ["corte rojo","pulsa espacio","gira izquierda"]
        current_step = 0
    draw_text(f"Instruccion: {instructions[current_step]}", 50)
    return "game10"

# ------------------- LOOP PRINCIPAL -------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.KEYDOWN:
            if current_game == "menu":
                if pygame.K_1 <= event.key <= pygame.K_9:
                    reset_all(); current_game = f"game{event.key-48}"
                if event.key == pygame.K_0:
                    reset_all(); current_game = "game10"
                if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()

            if current_game == "game3":
                for i,rect in enumerate(color_buttons):
                    if rect.collidepoint(mx,my):
                        if i == target_color_index: reset_all(); current_game="menu"
                        else: current_game="menu"

            if current_game == "game5":
                for b in falling_boxes[:]:
                    if b.collidepoint(mx,my): falling_boxes.remove(b)

            if current_game == "game6":
                for i,obj in enumerate(objects):
                    if obj.collidepoint(mx,my): current_game = "menu"

            if current_game == "game8":
                drawing.append((mx,my))

    # Lógica de escenas
    if current_game == "menu": game_menu()
    elif current_game == "game1": current_game = game_runner()
    elif current_game == "game2": current_game = game_memory()
    elif current_game == "game3": current_game = game_touch_color()
    elif current_game == "game4": current_game = game_timing()
    elif current_game == "game5": current_game = game_break_boxes()
    elif current_game == "game6": current_game = game_impostor()
    elif current_game == "game7": current_game = game_fishing()
    elif current_game == "game8": current_game = game_draw()
    elif current_game == "game9": current_game = game_coins()
    elif current_game == "game10": current_game = game_bomb()

    pygame.display.update()
    clock.tick(60)
