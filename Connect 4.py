import numpy as np
import pygame

ROW_NUM = 6
COLUMN_NUM = 7


def create_board():
    board = np.zeros((ROW_NUM, COLUMN_NUM))
    return board


def place_piece(board, col, row, piece):
    board[row][col] = piece


def is_valid_pos(board, col):
    return board[ROW_NUM - 1][col] == 0


def next_open_row(board, col):
    for r in range(ROW_NUM):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def check_win(board, piece):
    # CHECKING FOR HORIZONTAL WIN
    for c in range(COLUMN_NUM - 3):
        for r in range(ROW_NUM):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # CHECKING FOR VERTICAL WIN
    for c in range(COLUMN_NUM):
        for r in range(ROW_NUM - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # CHECKING FOR D+ve WIN
    for c in range(COLUMN_NUM - 3):
        for r in range(ROW_NUM - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # D-VE
    for c in range(3, COLUMN_NUM):
        for r in range(ROW_NUM - 3):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True


game_end = False
board = create_board()
print(board)
turn = 0

while not game_end:
    if turn == 0:
        col = int(input("Player 1, Choose A Position (0-7): ")) - 1
        if is_valid_pos(board, col):
            row = next_open_row(board, col)
            place_piece(board, col, row, 1)

        print_board(board)
        if check_win(board, 1):
            print('PLAYER 1 WON')
            game_end = True
        turn = 1

    elif turn == 1:
        col = int(input("Player 2, Choose A Position (0-7): ")) - 1
        if is_valid_pos(board, col):
            row = next_open_row(board, col)
            place_piece(board, col, row, 2)

        print_board(board)
        if check_win(board, 2):
            print('PLAYER 2 WON')
            game_end = True
        turn = 0
