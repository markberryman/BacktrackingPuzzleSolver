import backtrackingPuzzleSolver


sudoku = backtrackingPuzzleSolver.Sudoku()
board = backtrackingPuzzleSolver.board(3, 3, -1)
bps = backtrackingPuzzleSolver.BPS()
bps.solve(sudoku, board, None)

input("Press ENTER to exit.")
