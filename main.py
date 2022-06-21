import pygame
import time

pygame.init()


screen = pygame.display.set_mode((300,300))

# state variables
x = 50      # box x position
y = 150      # box y position
vx = 0
vy = 0

q2x = 10
q2y = 20
q2vx = 0.2
q2vy = 0.1
q2_is_inside_box = False
score = 0

def is_point_inside_box(x,y,w,h,px,py):
  if  (x + w > px > x) and (y + h > py > y):
    return True
  else:
    return False



while True:

  # render
  pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))  
  pygame.draw.rect(screen, (0,255,0),   (x,y,50,50))
  if q2_is_inside_box:
    pygame.draw.rect(screen, (0,0,255),   (q2x,q2y,10,10))
  else:
    pygame.draw.rect(screen, (255,0,0),   (q2x,q2y,10,10))


  
  pygame.display.flip() # draw everything
  time.sleep(0.02)

  # linear motion
  x = x + vx
  y = y + vy

  q2x = q2x + q2vx
  q2y = q2y + q2vy

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

  if q2x > 300:
    q2x = 0
  if q2y > 300:
    q2y = 0

  if is_point_inside_box(x,y,50,50,
                        q2x, q2y) and \
     is_point_inside_box(x,y,50,50,
                        q2x+10, q2y+10):
    q2_is_inside_box = True
                          
  else:
    q2_is_inside_box = False

  if keys[pygame.K_SPACE]:
    #print("space premuto")
    if q2_is_inside_box == True:
      q2x = 10000
      q2y = 10000
      score = score + 1