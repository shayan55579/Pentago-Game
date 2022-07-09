        if board.gameMode == 'ai' and board.player == 2:
            
            pygame.display.update()

            row,col = ai.evaluate(game)
            game.mark_squers(row, col, board.player)
            board.draw_fig(WIN, row+1, col+1)
            board.next_turn()