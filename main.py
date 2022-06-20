import pygame
import time

pygame.init()

x = 0
screen = pygame.display.set_mode((300,300))

vx = 3
while True:
  pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))
  
  pygame.draw.rect(screen, (0,255,0),   (x,0,50,50))
  
  pygame.display.flip() # draw everything
  time.sleep(0.02)
  
  x = x + vx

  # se l'oggetto sta uscendo dal mondo: esegui vx = -vx
  if x + 50 > 300:
    vx = -vx

  if x < 0:
    vx = -vx
    