import pygame
from .constans import *
from .game import Game
from .AI import AI
class Board:
    def __init__(self):
        self.game = Game()
        self.ai = AI()
        self.player = 1 #1-BlackCircle #2-RedCircle
        self.running = True
        self.gameMode = 'ai'
        self.ai =AI()


    #draw 4 rec 
    def draw_rec(self,win):
        win.fill(BG_COLOR)
        pygame.draw.rect(win, BLUE, pygame.Rect(50, 50, 300, 300),border_radius=50)
        pygame.draw.rect(win, BLUE, pygame.Rect(355, 50, 300, 300),border_radius=50)
        pygame.draw.rect(win, BLUE, pygame.Rect(50, 355, 300, 300),border_radius=50)
        pygame.draw.rect(win, BLUE, pygame.Rect(355, 355, 300, 300),border_radius=50)

    #draw 9 circles in rec
    def draw_circles(self, win):
        #x sabet bashe
        # pygame.draw.circle(win, GREEN, (100, 100), 30,0)
        # pygame.draw.circle(win, GREEN, (200, 100), 30,0)
        # pygame.draw.circle(win, GREEN, (300, 100), 30,0)
        # #y sabet bashe
        # pygame.draw.circle(win, GREEN, (100, 200), 30,0)
        # pygame.draw.circle(win, GREEN, (100, 300), 30,0)
        # pygame.draw.circle(win, GREEN, (100, 400), 30,0)
        for col in range(1,7):
            for row in range(1,7):
                pygame.draw.circle(win, WHITE,((col*100),(row*100)), 30, 0)
    #draw 2 lines for board
    def draw_lines(self, win):
    
        pygame.draw.line(win, BLACK,(0,300),(800,300),5)
        pygame.draw.line(win, BLACK,(400,0),(400,600),5)
    def next_turn(self):
        self.player = self.player % 2 + 1

    def draw_fig(self,win,row,col):
        if self.player == 1:
            pygame.draw.circle(win, BLACK,((col*100),(row*100)), 30, 0)
        elif self.player == 2:
            pygame.draw.circle(win, RED,((col*100),(row*100)), 30, 0)
    
    
    def take_screen_shot_1(self,win):
        rect = pygame.Rect(50, 50, 300, 300)
        screenshot = pygame.Surface(rect.size)
        screenshot.blit(win, (0, 0), rect)
        img = pygame.image.save(screenshot, "screenshot.png")
        #rotate imge 90
        img = pygame.image.load("screenshot.png")
        img = pygame.transform.rotate(img, -90)
        #bilud image to screen
        win.blit(img, (50, 50))
    
    
    def take_screen_shot_2(self,win):
        rect = pygame.Rect(50, 50, 300, 300)
        screenshot = pygame.Surface(rect.size)
        screenshot.blit(win, (0, 0), rect)
        img = pygame.image.save(screenshot, "screenshot1.png")
        #rotate imge 270
        img = pygame.image.load("screenshot1.png")
        img = pygame.transform.rotate(img, 90)
        #bilud image to screen
        win.blit(img, (50, 50))