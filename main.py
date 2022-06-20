import pygame

pygame.init()

screen = pygame.display.set_mode((300,300))

pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))

pygame.display.flip() # draw everything