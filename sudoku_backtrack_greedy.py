board = [
    [3, 7, 0, 0, 0, 0, 0, 9, 0],
    [9, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 4, 2, 0, 0, 0, 6],
    [0, 0, 1, 0, 8, 4, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 6, 0, 0, 0, 5, 0],
    [0, 0, 6, 0, 0, 2, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 9],
    [0, 5, 0, 0, 0, 0, 4, 0, 0]
]


def print_board(board):
    print("")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == len(board[0]) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end=" ")
    print("")

# structure to store the data


class PositionData:
    def __init__(self, row, col, no_of_positions):
        self.r = row
        self.c = col
        self.n = no_of_positions

    def set_data(self, row, col, no_of_positions):
        self.r = row
        self.c = col
        self.n = no_of_positions


def count_choices(board, px, py):
    choices = [True]*10

    # checking row
    for i in range(9):
        choices[board[px][i]] = False

    # checking col
    for j in range(9):
        choices[board[j][py]] = False

    # checking current box
    cx = px//3
    cy = py//3

    for i in range(cx*3, cx*3+3):
        for j in range(cy*3, cy*3 + 3):
            choices[board[i][j]] = False

    return choices.count(True)


def check_valid(board, px, py):
    num = board[px][py]
    # checking row
    for i in range(9):
        if board[px][i] == num and py != i:
            return False

    # checking col
    for j in range(9):
        if board[j][py] == num and px != j:
            return False

    cx = px//3
    cy = py//3

    for i in range(cx*3, cx*3+3):
        for j in range(cy*3, cy*3+3):
            if px != i and py != j and board[i][j] == num:
                return False

    return True


def solve(board):

    best_position = PositionData(-1, -1, 100)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:

                choice_count = count_choices(board, i, j)
                if best_position.n > choice_count:
                    best_position.set_data(i, j, choice_count)

    if best_position.n == 100:
        # implies no best position found i.e no more empty cells remain
        return True

    px = best_position.r
    py = best_position.c

    for i in range(1, 10):

        board[px][py] = i
        if check_valid(board, px, py):

            if solve(board):
                return True

        board[px][py] = 0

    return False


def solve_sudoku(board):
    print(solve(board))
    print_board(board)
