import pygame

class Ship():
    def __init__(self,screen):
        # 初始化飞船，设置初始位置

        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        #获取外接矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #初始位置,屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def biitme(self):
        self.screen.blit(self.image,self.rect)