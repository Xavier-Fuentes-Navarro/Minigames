import pygame
pygame.init()

# --- CONFIGURACIÓN ---
ancho, alto = 1280, 720
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# --- CARGAR IMAGEN Y TEXTO ---
imagen = pygame.image.load("Sprites/dot.png").convert_alpha()
imagen = pygame.transform.scale(imagen, (35, 35))

imagen2 = pygame.image.load("Sprites/right-arrow.png").convert_alpha()
imagen2 = pygame.transform.scale(imagen2, (35, 35))

text = font.render("Esquiva las bolas con WASD o las flechas", True, (255, 255, 255))

#Monstruos
imagen3 = pygame.image.load("Sprites/epstein.png").convert_alpha()
imagen3 = pygame.transform.scale(imagen3, (50, 50))

# --- POSICIÓN INICIAL DE LA IMAGEN ---

# Limitar posición dentro de la pantalla
x = max(0,ancho // 2,50)
y = max(0, alto // 2,50)



# --- LOOP PRINCIPAL ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- MOVIMIENTO DE LA IMAGEN ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        imagen = pygame.transform.rotate(imagen2, 180)
        x -= 5
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        imagen = pygame.transform.rotate(imagen2, 0)
        x += 5
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        imagen = pygame.transform.rotate(imagen2, 90)
        y -= 5
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        imagen = pygame.transform.rotate(imagen2, 270)
        y += 5
    # Movimientos diagonales
    if keys[pygame.K_w] and ((keys[pygame.K_a] or keys[pygame.K_LEFT])):
        imagen = pygame.transform.rotate(imagen2, 135)
        
    if keys[pygame.K_w] and ((keys[pygame.K_d] or keys[pygame.K_RIGHT])):
        imagen = pygame.transform.rotate(imagen2, 45)

    if keys[pygame.K_s] and ((keys[pygame.K_a] or keys[pygame.K_LEFT])):
        imagen = pygame.transform.rotate(imagen2, 225)

    if keys[pygame.K_s] and ((keys[pygame.K_d] or keys[pygame.K_RIGHT])):
        imagen = pygame.transform.rotate(imagen2, 315)


    if keys[pygame.K_ESCAPE]:
        running = False

    # --- DIBUJAR ---
    screen.fill((234, 54, 230))        # Fondo
    screen.blit(imagen, (x, y))       # Imagen que se mueve
    screen.blit(text, (20, 20))       # Texto fijo en la esquina

    pygame.display.flip()
    clock.tick(240)

pygame.quit()
