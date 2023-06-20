import time
import sys


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    row, col = find_empty(board)
    if row == -1 and col == -1:
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False


def get_user_input():
    print("enter the number of lines in the sudoku board:")
    num_lines = int(input())
    print(f"enter the sudoku board ({num_lines} lines, enter 0 or . for empty cells):")
    board = []
    for i in range(num_lines):
        row = input(f"Row {i+1}: ")
        while len(row) != 9 or any(c not in "1234567890." for c in row):
            print("invalid input. Each row should contain exactly 9 digits (0-9) or '.' for empty cells.")
            row = input(f"row {i+1}: ")
        board.append([int(c) if c != "." else 0 for c in row])
    return board


def main():
    board = get_user_input()

    if solve_sudoku(board):
        print("solution:")
        print_board(board)
    else:
        print("no solution exists. Maybe the board is invalid?")


if __name__ == "__main__":
    main()
