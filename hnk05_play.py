import pygame, sys
from pygame.locals import *

class HomeScreen:

    homebackground_path = 'images/bigimages/homebackground2.jpeg'

    color_green = (0, 255, 0)
    color_red = (255, 0, 0)
    color_white = (255, 255, 255)
    color_character_backround = pygame.Color(255, 255, 255, 128)
    text1 = '传统日麻'
    FPS = 60
    ttf = 'ttf/1.ttf'
    surfacesize = (1086, 724)

    #def __init__(self):


    def run(self):

        pygame.init()
        homebackground = pygame.image.load(HomeScreen.homebackground_path)
        back_surface = homebackground.convert(homebackground)
        pygame.transform.scale(back_surface, HomeScreen.surfacesize)

        fpsClock = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode(HomeScreen.surfacesize)
        pygame.display.set_caption('hanako_mahjong')

        fontObj = pygame.font.Font(HomeScreen.ttf, 64)
        textSurfaceObj = fontObj.render(HomeScreen.text1, True, HomeScreen.color_red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200,150)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
            # 背景绘制
            DISPLAYSURF.blit(homebackground, (0, 0), )
            # 文字们的绘制
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            pygame.display.update()  # 刷新屏幕
            fpsClock.tick(HomeScreen.FPS)  # 帧数控制

if __name__ == '__main__':
    hs = HomeScreen()
    hs.run()


