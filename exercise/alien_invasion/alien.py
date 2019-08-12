import sys

import pygame

from settings import Settings

from ship import Ship


def run_game():
    # 初始化并创建屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    #背景色
    # bg_color=(129,216,207)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#?quit()and QUIT
                sys.exit()
        #
        screen.fill(bg_color)
        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()