#!/usr/bin/python3
"""
Solves the N-Queens puzzle.

Determines all possible solutions for placing N non-attacking queens on an NxN chessboard.

Example:
    $ ./nqueens_solver.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys

def initialize_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def deepcopy_chessboard(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(deepcopy_chessboard, board))
    return board

def get_solution_coordinates(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution

def mark_unattainable_positions(board, row, col):
    """Mark out positions on a chessboard where non-attacking queens cannot be placed.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # Mark out all forward positions
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark out all backward positions
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark out all positions below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark out all positions above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark out all positions diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark out all positions diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # Mark out all positions diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark out all positions diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-Queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.

    Returns:
        solutions (list): A list of lists of solutions.
    """
    if queens == len(board):
        solutions.append(get_solution_coordinates(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = deepcopy_chessboard(board)
            tmp_board[row][col] = "Q"
            mark_unattainable_positions(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens_solver.py N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)

