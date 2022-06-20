import pygame
import time

pygame.init()

screen = pygame.display.set_mode((300,300))

pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))

pygame.draw.rect(screen, (0,255,0),   (0,0,50,50))

pygame.display.flip() # draw everything
time.sleep(1)

pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))

pygame.draw.rect(screen, (0,255,0),   (10,0,50,50))

pygame.display.flip()