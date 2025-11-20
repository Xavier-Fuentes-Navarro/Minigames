#El juego consite simplemente en no tocar el boton si lo tocas explota 
import pygame
import random
import math
d1=1280
d2=720
pygame.init()
screen = pygame.display.set_mode((d1, d2))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
# --- CARGAR IMAGEN Y TEXTO ---
