import pygame
pygame.init()

# --- CONFIGURACIÓN ---
ancho, alto = 1280, 720
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# --- CARGAR IMAGEN Y TEXTO ---
imagen = pygame.image.load("Sprites/dot.png").convert_alpha()
imagen = pygame.transform.scale(imagen, (51, 51))

imagen2 = pygame.image.load("Sprites/right-arrow.png").convert_alpha()
imagen2 = pygame.transform.scale(imagen2, (50, 50))

text = font.render("Esquiva las bolas con WASD o las flechas", True, (255, 255, 255))

# Monstruos
imagen3 = pygame.image.load("Sprites/epstein.png").convert_alpha()
imagen3 = pygame.transform.scale(imagen3, (50, 50))

# --- POSICIÓN INICIAL DEL JUGADOR ---
x, y = ancho // 2, alto // 2

# Limitar posición dentro de la pantalla
x = max(0, min(ancho - imagen.get_width(), x))
y = max(0, min(alto - imagen.get_height(), y))

# --- POSICIÓN INICIAL DEL MONSTRUO ---
x3, y3 = 100, 100

# --- FUNCIONES ---
def seguir_jugador(px, py, mx, my, v):
    """Devuelve nueva posición del monstruo moviéndose hacia el jugador"""
    dx = px - mx
    dy = py - my
    distancia = (dx**2 + dy**2)**0.5
    if distancia != 0:
        mx += v * dx / distancia
        my += v * dy / distancia
    return mx, my

# --- LOOP PRINCIPAL ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- MOVIMIENTO DEL JUGADOR ---
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    angle = 0

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx -= 5
        angle = 180
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx += 5
        angle = 0
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dy -= 5
        angle = 90
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dy += 5
        angle = 270

    # Diagonales
    if dx != 0 and dy != 0:
        if dx > 0 and dy < 0:
            angle = 45
        elif dx < 0 and dy < 0:
            angle = 135
        elif dx < 0 and dy > 0:
            angle = 225
        elif dx > 0 and dy > 0:
            angle = 315

    x += dx
    y += dy

    # Limitar dentro de pantalla
    x = max(0, min(ancho - imagen.get_width(), x))
    y = max(0, min(alto - imagen.get_height(), y))

    # --- SEGUIR JUGADOR ---
    x3, y3 = seguir_jugador(x, y, x3, y3, 2)  # Velocidad del monstruo

    # --- DIBUJAR ---
    screen.fill((0, 255, 0))           # Fondo
    rotated_image = pygame.transform.rotate(imagen2, angle)
    screen.blit(rotated_image, (x, y)) # Jugador
    screen.blit(imagen3, (x3, y3))     # Monstruo
    screen.blit(text, (20, 20))        # Texto

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
