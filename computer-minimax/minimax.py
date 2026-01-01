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
def get_player_move():
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1

            # check if the move is within the valid range
            if move < 0 or move > 8:
                print("Choose a number between 1 and 9.")
                continue

            # check if the chosen position is empty
            if board[move] != " ":
                print("That position is already taken.")
                continue

            return move
        
        except ValueError:
            print("Please enter a valid number.")


# recursively simulates every possible game outcome
def minimax(is_ai_turn):

    # base cases (game over)
    if check_winner("O"):
        return 1 # AI wins
    if check_winner("X"):
        return -1 # player wins
    if is_board_full():
        return 0 # draw

    if is_ai_turn:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


# determines best move for AI by evaluating all possibilities
def ai_move():

    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X. The AI is O.")
    print("Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board()

        # player turn
        move = get_player_move()
        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("You win!")
            break

        if is_board_full():
            print_board()
            print("It's a draw!")
            break

        # AI turn
        ai_move()

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if is_board_full():
            print_board()
            print("It's a draw!")
            break


play_game()
