import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'

pygame.init()
screen = pygame.display.set_mode((480, 320), 0, 32)
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key ==K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((480, 320), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((480, 320), 0, 32)

    screen.blit(background, (0, 0))  # 将内容显示出来
    pygame.display.update()  # 刷新屏幕
