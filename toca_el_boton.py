#El juego consite simplemente en tocas muchos
import random
import math
import pygame
#DEFINIMOS FIMERNISONS
d1=1280
d2=720
pygame.init()
#INICAMOS EL MIXER DE SONIDOS
pygame.mixer.init()
mensaje = "No toques el botón"
#PONER el mensaje en la ventana
pygame.display.set_caption(mensaje)

screen = pygame.display.set_mode((d1, d2))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
#CARGAR IMAGEN Y TEXTO
imagen = pygame.image.load("Sprites/boton.png").convert_alpha()
imagen = pygame.transform.scale(imagen,(200,200))
#pOSICIÓN INICIAL DEL BOTÓN
x,y = d1//2 -100, d2//2 -100
#LOOP PRINCIPAL 
#Contador de veceres que tocas el boton
count=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Obtener la posición del ratón
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Verificar si el ratón está sobre el botón:
    if x < mouse_x < x + 200 and y < mouse_y < y + 200 and pygame.mouse.get_pressed()[0]:
        # Reproducir sonido de explosión
        sonido_explosion = pygame.mixer.Sound("Sonidos/explosion2.wav")
        sonido_explosion.play()
        #Bajamos el volumen del sonido de explosion
        sonido_explosion.set_volume(0.04)
        
        # Mover el botón a una posición aleatoria
        y = random.randint(0, d2 - 200)
        x = random.randint(0, d1 - 200)
        count+=1
    
        
    # --- DIBUJAR ---
    texto_contador = font.render(f"Veces que has explotado: {count}", True, (32, 0, 0))
    #En fuente estilo new goofy
    font = pygame.font.SysFont("New Goofy", 30)
    screen.fill((255, 255, 255)) #fondo color blanco
    screen.blit(imagen, (x, y))
    screen.blit(texto_contador, (10, 10))
    pygame.display.flip()
    clock.tick(60)
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False
# --- IGNORE ---
pygame.quit()
