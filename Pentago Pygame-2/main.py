import pygame

from Pentago.constans import *

from Pentago.board import Board

from Pentago.game import Game


pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pentago")


def main():
    run = True
    # clock = pygame.time.Clock()
    board = Board()
    game = Game()
    ai = board.ai
    board.draw_rec(WIN)
    board.draw_circles(WIN)
    
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.take_screen_shot_1(WIN)
                    
                    game.rotate_1()
                    print("------------------------------------------------------")
                    print(game.squers)
                if event.key == pygame.K_RIGHT:
                    board.take_screen_shot_2(WIN)
                    game.rotate_2()
                    print(game.squers)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // CIRCLE_SIZE
                col = pos[0] // CIRCLE_SIZE
                if game.emty_squers(row, col):
                    game.mark_squers(row, col, board.player)
                    if game.check_horizontal() or game.check_vertical() or game.check_diagonal() :
                        print("Player " + str(board.player) + " wins!")
                        run = False
                    print("row:", row, "col:", col,"player:", board.player)

                    board.draw_fig(WIN, row+1, col+1)

                    board.next_turn() 
                    print(game.squers)
        if board.gameMode == 'ai' and board.player == 2 and board.running:
            
            pygame.display.update()

            row,col = ai.evaluate(game)
            game.mark_squers(row, col, board.player)
            board.draw_fig(WIN, row+1, col+1)
            board.next_turn()
                
        
        

        pygame.display.update()
    pygame.quit()


main()