from .constants import RED, BLUE,BLACK,WHITE,GREEN

class Piece:
    def __init__(self,row,col,color):

        PADDING = 10
        OUTLINE = 2
        self.row = row
        self.col = col
        self.color = color
        self.direction = 1


    def draw(self,win):
        radius = int(SQUARE_SIZE/2 - PADDING)
        pygame.draw.circle(win, GREEN, (self.col*SQUARE_SIZE + SQUARE_SIZE//2, self.row*SQUARE_SIZE + SQUARE_SIZE//2), radius)