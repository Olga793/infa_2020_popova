# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:41:30 2020

@author: Ольга
"""
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)

circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 0), (200, 200), 190, 0)
circle(screen, (255, 0, 0), (250, 150), 40, 0)
circle(screen, (255, 0, 0), (150, 150), 40, 0)
circle(screen, (0, 0, 0), (250, 150), 40, 1)
circle(screen, (0, 0, 0), (150, 150), 40, 1)
circle(screen, (0, 0, 0), (250, 150), 20, 0)
circle(screen, (0, 0, 0), (150, 150), 20, 0)
line(screen, (0, 0, 0), (120, 300), (270, 300), 30)
line(screen, (0, 0, 0), (100, 100), (190, 120), 20)
line(screen, (0, 0, 0), (200, 120), (300, 100), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()