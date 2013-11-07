import backtrackingPuzzleSolver


sudoku = backtrackingPuzzleSolver.Sudoku()
board = [[-1 for x in range(2)] for x in range(2)]
bps = backtrackingPuzzleSolver.BPS()
bps.solve(sudoku, board, None)
