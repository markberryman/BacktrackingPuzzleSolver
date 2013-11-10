# todo - figure out how to avoid passing entire board around w/ each attempt
# todo - advantage of using numpy matrix over 2-d array made by lists?
# todo - instead of board.rows property; make the board obj iterable?
import copy


class BPS(object):
    """Given a 2-D board type puzzle, solves it using recursion and backtracking."""

    def solve(self, puzzle, board):
        if (puzzle.is_solved(board)):
            puzzle.print_board(board)
            return True

        # find next square to "solve"
        # try all possible valid moves and recurse
        possible_moves = puzzle.get_possible_moves(puzzle, board)

        for move in possible_moves:
            # need to copy the board so we don't have separate
            # solution investigations stomp on each other
            new_board = copy.deepcopy(board)

            puzzle.make_move(move, new_board)
            
            puzzle_solved = self.solve(puzzle, new_board)

            if (puzzle_solved):
                return True

        # couldn't solve puzzle
        return False


class TwoDimBoardPuzzle(object):
    def is_solved(self, board):
        raise NotImplementedError()

    def get_possible_moves(self, puzzle, board):
        raise NotImplementedError()

    def make_move(self, move, board):
        raise NotImplementedError()

    def print_board(self, board):
        raise NotImplementedError()


class Sudoku(TwoDimBoardPuzzle):
    def is_solved(self, board):
        # board filled with valid values (i.e., no initialization values present)
        for row in board.rows:
            if (board.init_value in row):
                return False

        return True

    def get_possible_moves(self, puzzle, board):        
        unsolved_row = None
        unsolved_col = None
        possible_moves = []

        # figure out next square to solve
        for row in range(board.height):
            for col in range(board.width):
                if (board.rows[row][col] == board.init_value):
                    unsolved_row = row
                    unsolved_col = col
                    break

            if (unsolved_row is not None):
                break
        
        # possible moves for a sqaure includes all values not
        # already used in the current row, column or sub-region
        possible_values = [v for v in range(1, board.width + 1)]

        # removing row conflicts
        for row_val in board.rows[unsolved_row]:
            if row_val in possible_values:
                possible_values.remove(row_val)
        
        # removing col conflicts
        for col_val in [row[unsolved_col] for row in board.rows]:
            if col_val in possible_values:
                possible_values.remove(col_val)

        # removing sub-region conflicts
        # determine boundaries of sub-region
        col_sub_region = unsolved_col // board.sub_region_width
        row_sub_region = unsolved_row // board.sub_region_height

        sub_region_left_col = col_sub_region * board.sub_region_width
        sub_region_right_col = sub_region_left_col + (board.sub_region_width - 1)
        sub_region_top_row = row_sub_region * board.sub_region_height        
        sub_region_bottom_row = sub_region_top_row + (board.sub_region_height - 1)

        for row in range(sub_region_top_row, sub_region_bottom_row + 1):
            for col in range(sub_region_left_col, sub_region_right_col + 1):
                if (board.rows[row][col] in possible_values):
                    possible_values.remove(board.rows[row][col])

        for possible_value in possible_values:
            move = {}
            move["row"] = unsolved_row
            move["col"] = unsolved_col                    
            move["value"] = possible_value
            possible_moves.append(move)

        return possible_moves
        
    def make_move(self, move, board):
        board.rows[move["row"]][move["col"]] = move["value"]

    def print_board(self, board):
        for row in range(board.height):
            for col in range(board.width):
                print("{} ".format(board.rows[row][col]), end="")

            print()


class TwoDimensionalBoard(object):
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

class SudokuBoard(TwoDimensionalBoard):
    def __init__(self, width, height, sub_region_width, sub_region_height, init_value):
        super(SudokuBoard, self).__init__(width, height, init_value)        
        self._sub_region_width = sub_region_width
        self._sub_region_height = sub_region_height
        
    @property
    def sub_region_width(self):
        return self._sub_region_width

    @property
    def sub_region_height(self):
        return self._sub_region_height