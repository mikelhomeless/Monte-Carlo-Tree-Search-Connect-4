class InvalidMoveError(Exception):
    def __init__(self, message):
        self.message = "An invalid move was attempted. Column {} does not exist".format(message)

class FullColumnError(InvalidMoveError):
    def __init__(self, message):
        self.message = "An invalid move was attempted. Column {} is full".format(message)

class UnionFind:
    def __init__(self, size):
        self.size = size
        self.data = [-1] * self.size

    def union(self, n1, n2):
        n1_size, n1_parent = self.find(n1)
        n2_size, n2_parent = self.find(n2)
        min_indx, max_indx = self.min_max_parent_size(n1_size, n1_parent, n2_size, n2_parent)

        # Add the sizes of the two parent nodes together then set that value to the node with the largest size
        self.data[max_indx] = n1_size + n2_size

        # link the smallest sized node to the maximum sized node
        self.data[min_indx] = max_indx
        return self.data[max_indx]

    def find(self, n):
        # returns size of the equivalency set and parent node index
        while self.data[n] >= 0:
            n = self.data[n]
        return self.data[n], n

    def min_max_parent_size(self, n1_size, n1_indx, n2_size, n2_indx):
        if n1_size <= n2_size:
            return n2_indx, n1_indx
        else:
            return n1_indx, n2_indx

class ConnectFour:
    EQUIVALENCY_AXIES = [
        [(-1, 1),  (1, -1)],  # \ Diagonal
        [(-1, -1), (1, -1)],  # / Diagonal
        [(-1, 0),  (1, 0)],   # Horizontal axis
        [(0, -1)]             # Verticle axis
    ]

    def __init__(self):
        self.player_eq_set = [UnionFind(49 * 4), UnionFind(49 * 4)]
        self.__board = [[] for x in range(7)]
        self.current_player = 0

    def get_legal_moves(self):
        # If this function returns an empty list, there are no legal moves left; The game is over.
        return [indx for indx,x in enumerate(self.__board) if len(x) < 7]

    def __check_win(self, column):
        for eq_set_index_offset, axis in enumerate(self.EQUIVALENCY_AXIES):
            for offset in axis:
                row = len(self.__board[column]) - 1
                offset_coords = (column + offset[0], row + offset[1])
                offset_is_inbounds = 0 <= offset_coords[0] < 7 and 0 <= offset_coords[1] < 7
                try:
                    if offset_is_inbounds and self.__board[offset_coords[0]][offset_coords[1]] == self.current_player:
                        size = self.expand_equivalency_set(row, column, offset, eq_set_index_offset)
                        if abs(size) >= 4: return True
                except IndexError:
                    pass

    def expand_equivalency_set(self, row, column, offset, eq_set_index_offset):
        offset_coords = (column + offset[0], row + offset[1])

        flattend_coords = (28 * row) + (4 * column) + eq_set_index_offset
        flattend_offset_coords = (28 * offset_coords[1]) + (4 * offset_coords[0]) + eq_set_index_offset
        return self.player_eq_set[self.current_player].union(flattend_coords, flattend_offset_coords)

    # Returns whether or not the move resulted in a win
    def make_move(self, column):
        if self.is_valid_move(column):
            self.__board[column].append(self.current_player)
            return self.__check_win(column)

    def next_turn(self):
        self.current_player ^= 1

    def is_valid_move(self, column):
        if column > 6:
            raise InvalidMoveError(column)

        if len(self.__board[column]) > 6:
            raise FullColumnError(column)

        return True
