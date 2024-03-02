game_board = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]


def display_game_board():
    print("\n")
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])
    print("\n")


print(display_game_board())


def player():
    player1 = "X"
    player2 = "O"