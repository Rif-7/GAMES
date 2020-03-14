# _______Global variables ______
is_game_still_going = True

winner = None

current_player = "X"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


def game_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    global is_game_still_going
    global current_player
    game_board()
    while is_game_still_going:
        handle_turns(current_player)
        game_ended()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " Won")
    elif winner == None:
        print("tie")


def handle_turns(current_player):
    print(current_player + " 's turn")
    position = input("Choose a position from 1-9 : ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9 : ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Try again")
    board[position] = current_player
    game_board()


def game_ended():
    check_win()
    check_tie()


def check_win():
    global winner
    column_winner = check_columns()
    row_winner = check_rows()
    diagnal_winner = check_diagnals()
    if column_winner:
        winner = column_winner
    elif row_winner:
        winner = row_winner
    elif diagnal_winner:
        winner = diagnal_winner
    else:
        winner = None
    return


def check_rows():
    global board
    global winner
    global is_game_still_going
    r1 = board[0] == board[1] == board[2] != "-"
    r2 = board[3] == board[4] == board[5] != "-"
    r3 = board[6] == board[7] == board[8] != "-"
    if r1 or r2 or r3:
        is_game_still_going = False
    if r1:
        return board[0]
    elif r2:
        return board[3]
    elif r3:
        return board[6]
    return


def check_columns():
    global board
    global is_game_still_going
    global winner
    c1 = board[0] == board[3] == board[6] != "-"
    c2 = board[1] == board[4] == board[7] != "-"
    c3 = board[2] == board[5] == board[8] != "-"
    if c1 or c2 or c3:
        is_game_still_going = False
        if c1:
            return board[0]
        elif c2:
            return board[1]
        elif c3:
            return board[2]
        return


def check_diagnals():
    global board
    global winner
    global is_game_still_going
    d1 = board[0] == board[4] == board[8] != "-"
    d2 = board[2] == board[4] == board[6] != "-"
    if d1 or d2:
        is_game_still_going = False
        if d1:
            return board[0]
        elif d2:
            return board[2]
        return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def check_tie():
    global is_game_still_going
    if "-" not in board:
        is_game_still_going = False
    return


play_game()
