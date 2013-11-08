# todo - bug w/ sudoku board of size 3 x 3
# todo - figure out how to avoid passing entire board around w/ each attempt
# todo - make sense to consolidate move validity check w/ making the move?
# todo - move board creation to the puzzle logic?
# todo - better way to indicate no possible move other than length check of dict?
# todo - for sudoku, let's be explicit about the init value, min and max value; too much of a hack otherwise
# todo - advantage of using numpy matrix over 2-d array made by lists?
# todo - instead of board.rows property; make the board obj iterable?
import copy


class BPS(object):
    """Given a 2-D board type puzzle, solves it using recursive backtracking."""

    def solve(self, puzzle, board, move):
        if (puzzle.is_solved(board)):
            puzzle.print_board(board)
            return True

        while (True):
            print("*****************")
            puzzle.print_board(board)
            print("*****************")
            move = puzzle.get_next_move(move, board)

            if (len(move) != 0):
                #print("Trying move: row - {}, col - {}, val - {}".format(move["row"], move["col"], move["value"]))

                is_move_good = puzzle.is_move_valid(move, board)

                if (is_move_good):
                    #print("Move valid. Going to recurse.")

                    puzzle.make_move(move, board)

                    # need to copy the board so we don't have separate
                    # solution investigations stomp on each other
                    new_board = copy.deepcopy(board)

                    was_puzzle_solved = self.solve(puzzle, new_board, move)

                    if (was_puzzle_solved):
                        return True
                    else:
                        # get the next move as the last one turned
                        # out to be invalid
                        move["is_good"] = False
                else:
                    # move not valid, going to try next move
                    #print("Move *not* valid.")
                    pass
            else:
                # we're stuck, can't make another move; bail on this
                # solution search path
                #print("Stuck. Backtracking...")
                return False
            
        # made it here, means we couldn't solve the puzzle
        # down this current path of moves
        return False


class TwoDimBoardPuzzle(object):
    def is_move_good(self, move, board):
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
        col_conflict = (move["value"] not in [row[move["col"]] for row in board.rows])
        row_conflict = (move["value"] not in board.rows[move["row"]])

        result = col_conflict and row_conflict

        #result = ((move["value"] not in [row[move["col"]] for row in board.rows]) and
        #          (move["value"] not in board.rows[move["row"]]))

        move["is_good"] = result

        return result

    def is_solved(self, board):
        # board filled with valid values (i.e., no initialization values present)
        for row in board.rows:
            if (board.init_value in row):
                return False

        return True

    def get_next_move(self, move, board):
        next_move = {}

        # if the last move was not valid, we'll stay 
        # in the same square but try the next largest number (if possible)
        if (move["is_good"] is False):
            if (move["value"] < board.width):
                # try the next value for this current location
                next_move["col"] = move["col"]
                next_move["row"] = move["row"]
                next_move["value"] = move["value"] + 1
            # else, no next move for this square; out of values to try
        else:
            # last move was valid, proceed to next square that needs to be
            # solved
            square_to_check_idx = (move["row"] * board.width) + move["col"]

            while (board.rows[square_to_check_idx // board.height][square_to_check_idx % board.width] != board.init_value):
                square_to_check_idx += 1

            next_move["row"] = square_to_check_idx // board.height
            next_move["col"] = square_to_check_idx % board.width

            # bump up the column unless we're at the end of a row
            #if (move["col"] == (board.width - 1)):
            #    # at end of row
            #    next_move["col"] = 0
            #    next_move["row"] = move["row"] + 1
            #else:
            #    # not at end of row, bump up column
            #    next_move["col"] = move["col"] + 1
            #    next_move["row"] = move["row"]
                    
            next_move["value"] = 1

        return next_move
        
    def make_move(self, move, board):
        board.rows[move["row"]][move["col"]] = move["value"]

    def print_board(self, board):
        for row in range(board.height):
            for col in range(board.width):
                print("{} ".format(board.rows[row][col]), end="")

            print()


class board(object):
    def __init__(self, width, height, init_value):
        self._board = [[init_value for x in range(width)] for x in range(height)]
        self._width = width
        self._height = height
        self._init_value = init_value

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def init_value(self):
        return self._init_value

    @property
    def rows(self):
        return self._board
