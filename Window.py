import pygame

pygame.init()  # khoi tao module

screen = pygame.display.set_mode((1100, 550))


def window():
    icon = pygame.image.load('one.png')  # Icon game
    pygame.display.set_icon(icon)

    background = pygame.image.load('oẳn tù tì.png')  # bg game
    screen.blit(background, (450, 0))

    lineIMG = pygame.image.load('linee.png')  # tọa độ của đường thẳng
    screen.blit(lineIMG, (0, 420))

    guideIMG = pygame.image.load('guidee.png')  # tọa độ của hướng dẫn
    screen.blit(guideIMG, (0, 0))


window()


# tọa độ của ảnh win :
def win():
    winIMG = pygame.image.load('winn.png')
    screen.blit(winIMG, (370, 150))


# tọa độ của ảnh lose :
def lose():
    loseIMG = pygame.image.load('losee.png')
    screen.blit(loseIMG, (390, 150))


# tọa độ của ảnh hòa :
def same():
    drawIMG = pygame.image.load('draw.png')
    screen.blit(drawIMG, (390, 150))


win()
lose()
same()
