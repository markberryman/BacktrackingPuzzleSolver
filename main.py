import backtrackingPuzzleSolver


sudoku = backtrackingPuzzleSolver.Sudoku()
board = [[-1 for x in range(3)] for x in range(3)]
bps = backtrackingPuzzleSolver.BPS()
bps.solve(sudoku, board, None)

input("Press ENTER to exit.")
