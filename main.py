import random

import pygame  # thư viện pygame
import sys
from pygame import mixer  # nhạc nền
from pygame.locals import *  # khởi tạo tất cả chức năng của pygame

import Computer  # máy tính xử lý
import User  # tọa độ
import Window  # hiển thị màn hình

pygame.init()

screen = pygame.display.set_mode((1100, 550))  # tạo cửa sổ game
pygame.display.set_caption('Rock Paper Scissors - Nhóm 10')

clock = pygame.time.Clock()  # FPS

mixer.music.load('neonon-109616.mp3')  # music
mixer.music.play(-1)


# Ấn X để out game
def main():
    score = 0

    while True:

        font = pygame.font.SysFont('time', 24)
        show_score = font.render("Score : " + str(score), True, (255, 0, 0))  # tính điểm

        def show():
            screen.blit(show_score, (999, 0))

        screen.fill((255, 255, 255))  # vẽ màn hình trắng
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                print(event.key)

                # Ấn A ra búa :
                if event.key == K_a:
                    print(User.Rock())

                    # Kết quả khi ra búa :
                    computer = random.randint(1, 3)
                    if computer == 1:
                        print(Computer.rock1(), Window.same())

                    elif computer == 2:
                        print(Computer.scissors1(), Window.win())
                        score += 1  # win +1
                        show_score = font.render("Score : " + str(score), True, (255, 0, 0))

                    elif computer == 3:
                        print(Computer.paper1(), Window.lose())

                # Ấn D ra bao :
                if event.key == K_d:
                    print(User.Paper())

                    # Kết quả khi ra bao
                    computer = random.randint(1, 3)
                    if computer == 1:
                        print(Computer.rock1(), Window.win())
                        score += 1
                        show_score = font.render("Score : " + str(score), True, (255, 0, 0))

                    elif computer == 2:
                        print(Computer.scissors1(), Window.lose())

                    elif computer == 3:
                        print(Computer.paper1(), Window.same())

                # Ấn S ra kéo :
                if event.key == K_s:
                    print(User.Scissors())

                    # Kết quả khi ra kéo :
                    computer = random.randint(1, 3)
                    if computer == 1:
                        print(Computer.rock1(), Window.lose())

                    elif computer == 2:
                        print(Computer.scissors1(), Window.same())

                    elif computer == 3:
                        print(Computer.paper1(), Window.win())
                        score += 1
                        show_score = font.render("Score : " + str(score), True, (255, 0, 0))

        show()
        Computer.IMG_cpt()
        User.user()
        Window.window()
        pygame.display.update()


if __name__ == '__main__':
    main()
