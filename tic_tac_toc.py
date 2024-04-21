import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def p_1_turn(board):
    while True:
        row = int(input("행 선택 (0, 1, 2): "))
        col = int(input("열 선택 (0, 1, 2): "))
        if board[row][col] == " ":
            return row, col
        else:
            print("다시 선택")

def com_turn(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def ttt():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for _ in range(9):
        print_board(board)

        if player == "X":
            row, col = p_1_turn(board)
            print("===============================")
        else:
            row, col = com_turn(board)
            print("===============================")

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            if player == "X":
                print("Player 승!")
            else:
                print("Computer 승!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("무승부")

ttt()
