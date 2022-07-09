from .constans import *
import random
from .game import Game
import copy
class AI:
    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    def rnd(self,board):
        game = Game()
        empty_sqrs = game.getEmptySquers()
        idx = random.randrange(0,len(empty_sqrs)-1)
        
        return empty_sqrs[idx]

    def minMax(self,board,maximizng):
        #terminal cases
        game = Game()
        case = game.final_state()
        #player 1 wins
        if case == 1:
            return 1, None#eval,move
        #player 2 wins
        if case == 2:
            return -1, None#eval,move
        #draw
        if case == 0:
            return 0, None#eval,move
        if maximizng:
            max_eval = -10
            best_move = None
            emty_squers = game.getEmptySquers()
            for (row,col) in emty_squers:
                temp_board = copy.deepcopy(board)
                temp_board.mark_squers(row, col, 1)
                eval = self.minMax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row,col)

            return max_eval, best_move  
        elif not maximizng:
            min_eval = 10
            best_move = None
            emty_squers = game.getEmptySquers()
            for (row,col) in emty_squers:
                temp_board = copy.deepcopy(board)
                temp_board.mark_squers(row, col, self.player)
                eval = self.minMax(temp_board, True)[0]
                if eval<min_eval:
                    min_eval = eval
                    best_move = (row,col)

            return min_eval, best_move  



    def evaluate(self, main_board):
        if self.level == 0:
            #random choice
            eval = 'ramdom'
            move = self.rnd(main_board)
        else:
            eval,move = self.minMax(main_board, False)

        print(f'AI has chosen {move} with eval of {eval}')
        return move #returns tuple (row,col)
        
