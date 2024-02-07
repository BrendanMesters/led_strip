import pygame
import sys

pygame.init()

screen = pygame.display.set_mode(200, 100)
pygame.display.set_caption("Heus wel een led strip")

screen.fill(black)
pygame.draw.circle(screen, (13, 250, 120), (20, 20), 10)

pygame.display.flip()
