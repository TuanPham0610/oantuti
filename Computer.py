import pygame

screen = pygame.display.set_mode((1100, 550))


# Tọa độ b,k,b góc phải màn hình :

def IMG_cpt():
    rockIMG = pygame.image.load('búaa.png')
    screen.blit(rockIMG, (1035, 450))

    paperIMG = pygame.image.load('baoo.png')
    screen.blit(paperIMG, (795, 440))

    scissorsIMG = pygame.image.load('kéoo.png')
    screen.blit(scissorsIMG, (915, 440))

IMG_cpt()


# --------------------------------------------------
# tọa độ búa cpt khi random ra :
def rock1():

    rock1IMG = pygame.image.load('buaa zoom.png')
    screen.blit(rock1IMG, (900, 200))


# tọa độ của bao cpt khi random ra :
def paper1():

    paper1IMG = pygame.image.load('baoo zoom.png')
    screen.blit(paper1IMG, (900, 200))


# tọa độ của kéo cpt khi random ra :
def scissors1():

    scissors1IMG = pygame.image.load('kéoo zoom.png')
    screen.blit(scissors1IMG, (900, 200))


rock1()
scissors1()
paper1()

