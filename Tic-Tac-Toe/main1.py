# Designing the game board
# Taking player inputs
# Alternating turns between players
# Checking for a win or a draw
# Ending and restarting the game

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


def player_input(player):
    # Take the player's input for a board position (1-9).
    position = int(input("Pick a position between 1 to 9: ")) - 1
    # Check if the chosen position is empty.
    if game_board[position] == " ":
        # Place the player's symbol in that position if it is valid.
        game_board[position] = player
    else:
        print("The position has been taken.")


def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for conditions in win_conditions:
        if
