from player import Agent
from game import ConnectFour
from view_controller import ConnectFourView

game = ConnectFour()
view = ConnectFourView()
players = [Agent(game, 50, 0), Agent(game, 1000, 1)]

while game.get_legal_moves():
    move = players[game.current_player].get_move()
    did_win = game.make_move(move)
    view.draw_board(game.board)
    if did_win:
        print('Player {} won'.format(game.current_player + 1))
        break
    game.next_turn()

if not game.get_legal_moves():
    print('It was a tie!')
