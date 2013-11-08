import backtrackingPuzzleSolver


sudoku = backtrackingPuzzleSolver.Sudoku()
board = backtrackingPuzzleSolver.board(4, 4, -1)
bps = backtrackingPuzzleSolver.BPS()
bps.solve(sudoku, board, None)

input("Press ENTER to exit.")
