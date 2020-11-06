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


def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def check_valid(board, num, pos):

    # check if row possible after placing number at pos(x,y)
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # checking along columns
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check the current box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and pos != (i, j):
                return False

    return True


def solve_sudoku(board):
    curr_pos = find_empty_cell(board)
    if not curr_pos:
        return True
    else:

        r, c = curr_pos

    for i in range(1, 10):
        if check_valid(board, i, curr_pos):
            board[r][c] = i

            if solve_sudoku(board):
                return True

            board[r][c] = 0

    return False


solve_sudoku(board)

print_board(board)
