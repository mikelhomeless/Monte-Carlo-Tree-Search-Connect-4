class ConnectFourView:

    def draw_board(self, board):
        render_list = [ [None] * 7 for x in range(7) ]
        for x in range(7):
            for y in range(len(board[x])):
                render_list[x][y] = board[x][y]

        formated_list = [ self.color_code(y) for x in render_list for y in x]
        formatted_string = ''
        for y in range(6, -1, -1):
            for x in range(7):
                formatted_string += formated_list[(7 * x) + y] + ' '
            formatted_string += '\n'
        print(formatted_string)

    def color_code(self, token):
        if token == 0:
            return "\033[1;31;40m X"
        if token == 1:
            return "\033[1;33;40m X"
        else:
            return "\033[1;37;40m *"

if __name__ == '__main__':
    array = [
    [],
    [],
    [0,0,1],
    [0],
    [1,1],
    [1],
    []
    ]

    renderer = ConnectFourView()
    renderer.draw_board(array)
