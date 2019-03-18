from math import log, sqrt
from copy import deepcopy
from copy import copy
from random import choice

class mtc_node:
    def __init__(self):
        self.wins = 0
        self.moves = 0
        self.agent_moves = 0
        self.loses = 0

    # def calculate_value(self, wins, moves, agent_moves):
    #     self.wins += wins
    #     self.moves += moves
    #     self.agent_moves += agent_moves
    #     self.value =

class Agent:

    # has a search depth variable
    # has a structure for keeping track of data from the monte carlo search
    def __init__(self, game, search_limit, player_number):
        self.player_num = player_number
        self.game = game
        self.search_limit = search_limit

    def get_move(self):
        # Copy over all state information
        current_board_state = deepcopy(self.game.board)
        current_player0_data = copy(self.game.player_eq_set[0].data)
        current_player1_data = copy(self.game.player_eq_set[1].data)

        legal_moves = self.game.get_legal_moves()
        if len(legal_moves) == 1:
            return legal_moves[0]

        move_stats = { key: mtc_node() for key in legal_moves }
        search_count = 0
        while search_count < self.search_limit:
            self.run_simulation(move_stats, choice(legal_moves))
            self.game.board = deepcopy(current_board_state)
            self.game.player_eq_set[0].data = copy(current_player0_data)
            self.game.player_eq_set[1].data = copy(current_player1_data)
            self.game.current_player = self.player_num
            search_count += 1

        try:
            move = max(move_stats, key=(lambda k: (move_stats[k].wins - move_stats[k].loses) / move_stats[k].agent_moves))
        except ZeroDivisionError:
            move = max(move_stats, key=(lambda k: move_stats[k].wins))
        return move

    def run_simulation(self, move_stats, orig_column):
        did_win = False
        did_lose = False
        legal_moves = self.game.get_legal_moves()
        move = orig_column
        while not did_win and not did_lose and legal_moves:
            did_win = self.game.make_move(move)
            move_stats[orig_column].agent_moves += 1
            move_stats[orig_column].moves += 1

            if did_win:
                move_stats[move].wins += 1
                return
            elif not self.game.get_legal_moves():
                return
            else:
                self.game.next_turn()
                legal_moves = self.game.get_legal_moves()
                move = choice(legal_moves)
                did_lose = self.game.make_move(move)
                move_stats[orig_column].moves += 1
                if did_lose:
                    move_stats[orig_column].loses += 1
                    return

            self.game.next_turn()
            legal_moves = self.game.get_legal_moves()
            if legal_moves:
                move = choice(legal_moves)
