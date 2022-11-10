import pygame

screen = pygame.display.set_mode((1100, 550))


def user():  # tọa độ hình ảnh b,k,b ở góc trái màn hình

    rockIMG = pygame.image.load('búaa.png')
    screen.blit(rockIMG, (0, 450))

    paperIMG = pygame.image.load('baoo.png')
    screen.blit(paperIMG, (230, 440))

    scissorsIMG = pygame.image.load('kéoo.png')
    screen.blit(scissorsIMG, (110, 440))

user()


# ----------------------------------------
# tọa độ b,k,b khi người dùng bấm

def Rock():
    rockIMG = pygame.image.load('buaa zoom.png')
    screen.blit(rockIMG, (110, 200))

Rock()


def Paper():
    paperIMG = pygame.image.load('baoo zoom.png')
    screen.blit(paperIMG, (110, 200))

Paper()


def Scissors():
    scissorsIMG = pygame.image.load('kéoo zoom.png')
    screen.blit(scissorsIMG, (110, 200))

Scissors()
