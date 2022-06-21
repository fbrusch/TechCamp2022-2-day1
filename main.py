import pygame
import time

pygame.init()


screen = pygame.display.set_mode((300,300))

# state variables
x = 50      # box x position
y = 150      # box y position
vx = 3
vy = 1

while True:

  # render
  pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))  
  pygame.draw.rect(screen, (0,255,0),   (x,y,50,50))
  
  pygame.display.flip() # draw everything
  time.sleep(0.02)

  # linear motion
  x = x + vx
  y = y + vy

  # friction
  #vx = vx*0.98
  #vy = vy*0.98
  
  # vy = vy + 0.3

  # spring in the center
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    vy = vy - 0.1
  if keys[pygame.K_DOWN]:
    vy = vy + 0.1
  if keys[pygame.K_LEFT]:
    vx = vx - 0.1
  if keys[pygame.K_RIGHT]:
    vx = vx + 0.1
    
  

  # se l'oggetto sta uscendo dal mondo: esegui vx = -vx
  if x + 50 > 300:
    vx = -vx

  if x < 0:
    vx = -vx

  if y + 50 > 300:
    vy = -vy

  if y < 0:
    vy = -vy
    