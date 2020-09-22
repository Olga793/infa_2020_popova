# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:01:14 2020

@author: Ольга
"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 0, 255), (0, 200, 400, 400))

circle(screen, (255, 255, 255), (340, 240), 30)
circle(screen, (0, 0, 0), (340, 240), 30, 1)
ellipse(screen, (255, 255, 255), (100, 200, 250, 100))
ellipse(screen, (0, 0, 0), (100, 200, 250, 100), 1)
circle(screen, (255, 255, 255), (120, 200), 50)
circle(screen, (0, 0, 0), (120, 200), 50, 1)
circle(screen, (255, 255, 255), (280, 270), 40)
circle(screen, (0, 0, 0), (280, 270), 40, 1)
ellipse(screen, (255, 255, 255), (300, 180, 50, 90))
ellipse(screen, (0, 0, 0), (300, 180, 50, 90), 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            finished = True

pygame.quit()