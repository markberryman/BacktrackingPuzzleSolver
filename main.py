import backtrackingPuzzleSolver
import time


def create_9x9_board():
    board = backtrackingPuzzleSolver.SudokuBoard(9, 9, 3, 3, 0)

    board.rows[0][0] = 5
    board.rows[0][1] = 3
    board.rows[0][2] = 0
    board.rows[0][3] = 0
    board.rows[0][4] = 7
    board.rows[0][5] = 0
    board.rows[0][6] = 0
    board.rows[0][7] = 0
    board.rows[0][8] = 0

    board.rows[1][0] = 6
    board.rows[1][1] = 0
    board.rows[1][2] = 0
    board.rows[1][3] = 1
    board.rows[1][4] = 9
    board.rows[1][5] = 5
    board.rows[1][6] = 0
    board.rows[1][7] = 0
    board.rows[1][8] = 0

    board.rows[2][0] = 0
    board.rows[2][1] = 9
    board.rows[2][2] = 8
    board.rows[2][3] = 0
    board.rows[2][4] = 0
    board.rows[2][5] = 0
    board.rows[2][6] = 0
    board.rows[2][7] = 6
    board.rows[2][8] = 0

    board.rows[3][0] = 8
    board.rows[3][1] = 0
    board.rows[3][2] = 0
    board.rows[3][3] = 0
    board.rows[3][4] = 6
    board.rows[3][5] = 0
    board.rows[3][6] = 0
    board.rows[3][7] = 0
    board.rows[3][8] = 3

    board.rows[4][0] = 4
    board.rows[4][1] = 0
    board.rows[4][2] = 0
    board.rows[4][3] = 8
    board.rows[4][4] = 0
    board.rows[4][5] = 3
    board.rows[4][6] = 0
    board.rows[4][7] = 0
    board.rows[4][8] = 1

    board.rows[5][0] = 7
    board.rows[5][1] = 0
    board.rows[5][2] = 0
    board.rows[5][3] = 0
    board.rows[5][4] = 2
    board.rows[5][5] = 0
    board.rows[5][6] = 0
    board.rows[5][7] = 0
    board.rows[5][8] = 6

    board.rows[6][0] = 0
    board.rows[6][1] = 6
    board.rows[6][2] = 0
    board.rows[6][3] = 0
    board.rows[6][4] = 0
    board.rows[6][5] = 0
    board.rows[6][6] = 2
    board.rows[6][7] = 8
    board.rows[6][8] = 0

    board.rows[7][0] = 0
    board.rows[7][1] = 0
    board.rows[7][2] = 0
    board.rows[7][3] = 4
    board.rows[7][4] = 1
    board.rows[7][5] = 9
    board.rows[7][6] = 0
    board.rows[7][7] = 0
    board.rows[7][8] = 5

    board.rows[8][0] = 0
    board.rows[8][1] = 0
    board.rows[8][2] = 0
    board.rows[8][3] = 0
    board.rows[8][4] = 8
    board.rows[8][5] = 0
    board.rows[8][6] = 0
    board.rows[8][7] = 7
    board.rows[8][8] = 9

    return board

def create_6x6_board():
    board = backtrackingPuzzleSolver.SudokuBoard(6, 6, 3, 2, 0)

    board.rows[0][0] = 0
    board.rows[0][1] = 5
    board.rows[0][2] = 1
    board.rows[0][3] = 6
    board.rows[0][4] = 0
    board.rows[0][5] = 2

    board.rows[1][0] = 2
    board.rows[1][1] = 0
    board.rows[1][2] = 0
    board.rows[1][3] = 0
    board.rows[1][4] = 0
    board.rows[1][5] = 0

    board.rows[2][0] = 0
    board.rows[2][1] = 0
    board.rows[2][2] = 0
    board.rows[2][3] = 0
    board.rows[2][4] = 0
    board.rows[2][5] = 4

    board.rows[3][0] = 3
    board.rows[3][1] = 0
    board.rows[3][2] = 0
    board.rows[3][3] = 0
    board.rows[3][4] = 0
    board.rows[3][5] = 0

    board.rows[4][0] = 0
    board.rows[4][1] = 0
    board.rows[4][2] = 0
    board.rows[4][3] = 0
    board.rows[4][4] = 0
    board.rows[4][5] = 1

    board.rows[5][0] = 1
    board.rows[5][1] = 0
    board.rows[5][2] = 4
    board.rows[5][3] = 2
    board.rows[5][4] = 5
    board.rows[5][5] = 0

    return board


sudoku = backtrackingPuzzleSolver.Sudoku()
#board = create_6x6_board()
board = create_9x9_board()

start_time = time.time()
bps = backtrackingPuzzleSolver.BPS()
bps.solve(sudoku, board)
end_time = time.time()

print("Took {} seconds.".format(end_time - start_time))

input("Press ENTER to exit.")
