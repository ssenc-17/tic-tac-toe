board = [" " for _ in range(9)]

# prints current state of board in readable format
def print_board():

    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


# checks whether given player has won
def check_winner(player):

    # all possible winning combinations
    winning_combinations = [
        (0, 1, 2), # top row
        (3, 4, 5), # middle row
        (6, 7, 8), # bottom row
        (0, 3, 6), # left column
        (1, 4, 7), # middle column
        (2, 5, 8), # right column
        (0, 4, 8), # main diagonal
        (2, 4, 6)  # other diagonal
    ]

    # check each winning combination
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

#checks whether the board is full
def is_board_full():
    return " " not in board


# prompts current player for their move
def get_player_move(player):

    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1

            # check if the move is within the valid range
            if move < 0 or move > 8:
                print("Please choose a number between 1 and 9.")
                continue

            # check if the chosen position is empty
            if board[move] != " ":
                print("That position is already taken. Try again.")
                continue

            return move

        except ValueError:
            print("Please enter a valid number.")

# main game loop
def play_game():

    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1 to 9 as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board()

        move = get_player_move(current_player)
        board[move] = current_player

        # check if the current player has won
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # check for a draw
        if is_board_full():
            print_board()
            print("It's a draw!")
            break

        # switch players
        current_player = "O" if current_player == "X" else "X"


play_game()
