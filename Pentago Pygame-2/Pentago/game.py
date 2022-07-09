import pygame
import numpy as np
from .constans import *

class Game:

    def __init__(self):
        self.squers = np.zeros((6,6))
        # self.emty_squer =self.squers
        self.marked_squers = 0

    def final_state(self):
        '''
                
            @return 0 if there is no win yet
            @return 1 if player 1 wins
            @return 2 if player 2 wins
        '''
        if self.check_horizontal() or self.check_vertical():
            return 1
        elif self.check_horizontal() or self.check_vertical():
            return 2
        else:
            return 0
        

    def mark_squers(self,rows,cols,player):
        self.squers[rows][cols] = player
        self.marked_squers += 1

    def emty_squers(self,rows,cols):
        return self.squers[rows][cols] == 0
    
    def getEmptySquers(self):
        empty_sqrs = []
        for row in range(6):
            for col in range(6):
                if self.squers[row][col] == 0:
                    
                    empty_sqrs.append((row,col))
        return empty_sqrs

    
    def isFull(self):
        return self.marked_squers == 36

    def isEmpty(self):
        return self.squers == 0

    def rotate_1(self):
        #swap elemnts by index
        #create switch case
        
        self.squers[0,0], self.squers[0,2] = self.squers[0,2], self.squers[0,0]
        self.squers[0,1], self.squers[1,2] = self.squers[0,1], self.squers[1,2]
        self.squers[0,2],self.squers[2,2] = self.squers[2,2], self.squers[0,2]
        self.squers[1,0],self.squers[0,1] = self.squers[0,1], self.squers[1,0]
        self.squers[1,2],self.squers[2,1] = self.squers[2,1], self.squers[1,2]
        self.squers[2,0],self.squers[0,0] = self.squers[0,0], self.squers[2,0]
        self.squers[2,1],self.squers[1,0] = self.squers[1,0], self.squers[2,1]
        self.squers[2,2],self.squers[2,0] = self.squers[2,0], self.squers[2,2]
    
    
    def rotate_2(self):
        #swap elemnts by index
        self.squers[0,0], self.squers[2,0] = self.squers[2,0], self.squers[0,0]
        self.squers[0,1], self.squers[1,0] = self.squers[1,0], self.squers[0,1]
        self.squers[0,2],self.squers[0,0] = self.squers[0,0], self.squers[0,2]
        self.squers[1,0],self.squers[2,1] = self.squers[2,1], self.squers[1,0]
        self.squers[1,2],self.squers[1,0] = self.squers[1,0], self.squers[1,2]
        self.squers[2,0],self.squers[2,2] = self.squers[2,2], self.squers[2,0]
        self.squers[2,1],self.squers[1,2] = self.squers[1,2], self.squers[2,1]
        self.squers[2,2],self.squers[0,2] = self.squers[0,2], self.squers[2,2]

    def rotate_3(self):
        #swap elemnts by index
        self.squers[0,3],self.squers[0,5] = self.squers[0,5], self.squers[0,3]
        self.squers[0,4],self.squers[1,5] = self.squers[0,4], self.squers[1,5]
        self.squers[0,5],self.squers[2,5] = self.squers[2,5], self.squers[0,5]
        self.squers[1,3],self.squers[2,4] = self.squers[2,4], self.squers[1,3]
        self.squers[1,5],self.squers[0,4] = self.squers[0,4], self.squers[1,5]
        self.squers[2,3],self.squers[2,5] = self.squers[2,5], self.squers[2,3]
        self.squers[2,4],self.squers[1,5] = self.squers[1,5], self.squers[2,4]
        self.squers[2,5],self.squers[0,5] = self.squers[0,5], self.squers[2,5]
    

        
    
    #check horizontal win for 5 elements
    def check_horizontal(self):
        for i in range(6):
            for j in range(2):
                if self.squers[i][j] == self.squers[i][j+1] == self.squers[i][j+2] ==self.squers[i][j+3] ==self.squers[i][j+4]  != 0:
                    return True

    # check vertical win
    def check_vertical(self):
        for i in range(2):
            for j in range(6):
                if self.squers[i][j] == self.squers[i+1][j] == self.squers[i+2][j] == self.squers[i+3][j] == self.squers[i+4][j] != 0:
                    return True
    #check diagonal win
    def check_diagonal(self):
        for i in range(2):
            for j in range(2):
                if self.squers[i][j] == self.squers[i+1][j+1] == self.squers[i+2][j+2] ==self.squers[i+3][j+3] ==self.squers[i+4][j+4] != 0:
                    return True
        for i in range(2):
            for j in range(2,6):
                if self.squers[i][j] == self.squers[i+1][j-1] == self.squers[i+2][j-2] ==self.squers[i+3][j-3] ==self.squers[i+4][j-4] != 0:
                    return True
 