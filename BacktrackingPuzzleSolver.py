# todo - figure out how to avoid passing entire board around w/ each attempt
# todo - make sense to consolidate move validity check w/ making the move?
# todo - move board creation to the puzzle logic?
import copy


class BPS(object):
    """Given a 2-D board type puzzle, solves it using recursive backtracking."""

    def solve(self, puzzle, board, last_move):
        if (puzzle.is_solved(board)):
            puzzle.print_board(board)
            return True

        while (True):
            # next move based on last move
            move = puzzle.get_next_move(last_move, board)

            if (move is not None):
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
        # checking for dupe in same column
        if (move["value"] in [row[move["col"]] for row in board]):
            return False
        
        # checking for dupe in same row
        if (move["value"] in board[move["row"]]):
            return False

        return True

    def is_solved(self, board):
        # board filled with valid values (i.e., no initialization values present)
        for row in board:
            if (-1 in row):
                return False

        return True

    def get_next_move(self, last_move, board):
        next_move = {}

        # might be the first move so no last move
        if (last_move is None):
            next_move["col"] = 0
            next_move["row"] = 0
            next_move["value"] = 1
        else:
            # exhaust #'s for a location before moving on
            if (last_move["value"] == len(board)):
                # need to move to next location
                if (last_move["col"] < (len(board) - 1)):
                    # moving a column over
                    next_move["col"] = last_move["col"] + 1
                    next_move["row"] = last_move["row"]
                    next_move["value"] = 1
                else:
                    # moving a row down if possible
                    if (last_move["row"] < (len(board[0]) - 1)):
                        next_move["col"] = last_move["col"]
                        next_move["row"] = last_move["row"] + 1
                        next_move["value"] = 1
                    # else, we've gone off the end of the board
            else:
                # try the next value for this current location
                next_move["col"] = last_move["col"]
                next_move["row"] = last_move["row"]
                next_move["value"] = last_move["value"] + 1

        return next_move
        
    def make_move(self, move, board):
        board[move["row"]][move["col"]] = move["value"]

    def print_board(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                print("{} ".format(board[row][col]), end="")

            print()
