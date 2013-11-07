# todo - bug w/ sudoku board of size 3 x 3
# todo - figure out how to avoid passing entire board around w/ each attempt
# todo - make sense to consolidate move validity check w/ making the move?
# todo - move board creation to the puzzle logic?
# todo - better way to indicate no possible move other than length check of dict?
# todo - for sudoku, let's be explicit about the init value, min and max value; too much of a hack otherwise
# todo - advantage of using numpy matrix over 2-d array made by lists?
import copy


class BPS(object):
    """Given a 2-D board type puzzle, solves it using recursive backtracking."""

    def solve(self, puzzle, board, last_move):
        if (puzzle.is_solved(board)):
            puzzle.print_board(board)
            return True

        while (True):
            move = puzzle.get_next_move(last_move, board)

            if (len(move) != 0):
                is_move_valid = puzzle.is_move_valid(move, board)

                if (is_move_valid):
                    # need to copy the board so we don't have separate
                    # solution investigations stomp on each other
                    new_board = copy.deepcopy(board)

                    puzzle.make_move(move, new_board)

                    was_puzzle_solved = self.solve(puzzle, new_board, move)

                    if (was_puzzle_solved):
                        return True
                    # else, we continue getting the next move
                else:
                    # move not valid, going to try next move
                    last_move = move
            else:
                # we're stuck, can't make another move; bail on this
                # solution search path
                return False
            
        # made it here, means we couldn't solve the puzzle
        # down this current path of moves
        return False


class TwoDimBoardPuzzle(object):
    def is_move_valid(self, move, board):
        raise NotImplementedError()

    def is_solved(self, board):
        raise NotImplementedError()

    def get_next_move(self, last_move, board):
        raise NotImplementedError()

    def make_move(self, move, board):
        raise NotImplementedError()

    def print_board(self, board):
        raise NotImplementedError()


class Sudoku(TwoDimBoardPuzzle):
    def is_move_valid(self, move, board):
        # besides checking the move's validity,
        # we're going to flag the move as well b/c
        # we need this info to determine the next move
        
        # checking for dupe in same column and row
        result = ((move["value"] not in [row[move["col"]] for row in board]) and
                  (move["value"] not in board[move["row"]]))

        move["is_valid"] = result

        return result

    def is_solved(self, board):
        # board filled with valid values (i.e., no initialization values present)
        for row in board:
            if (-1 in row):
                return False

        return True

    def get_next_move(self, last_move, board):
        next_move = {}

        if (last_move is None):
            # first move
            next_move["col"] = 0
            next_move["row"] = 0
            next_move["value"] = 1
        else:
            # if the last move was not valid, we'll stay 
            # in the same square but try the next largest number (if possible)
            if (last_move["is_valid"] is False):
                if (last_move["value"] < len(board)):
                    # try the next value for this current location
                    next_move["col"] = last_move["col"]
                    next_move["row"] = last_move["row"]
                    next_move["value"] = last_move["value"] + 1
                # else, no next move for this square; out of values to try
            else:
                # last move was valid, proceed to next square
                # bump up the column unless we're at the end of a row
                if (last_move["col"] == (len(board) - 1)):
                    # at end of row
                    next_move["col"] = 0
                    next_move["row"] = last_move["row"] + 1
                else:
                    # not at end of row, bump up column
                    next_move["col"] = last_move["col"] + 1
                    next_move["row"] = last_move["row"]
                    
                next_move["value"] = 1

        return next_move
        
    def make_move(self, move, board):
        board[move["row"]][move["col"]] = move["value"]

    def print_board(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                print("{} ".format(board[row][col]), end="")

            print()
