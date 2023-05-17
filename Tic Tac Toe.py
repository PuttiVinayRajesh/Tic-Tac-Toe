# Tic-Tac-Toe

# Create the game board
board = [" " for _ in range(9)]

# Function to print the game board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if the game is over
def is_game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
        return True
    
    # Check if the board is full
    if " " not in board:
        return True
    
    return False

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while not is_game_over():
        # Get the current player's input
        current_player = "X" if board.count("X") == board.count("O") else "O"
        print("It's", current_player, "'s turn.")
        position = int(input("Enter a position (1-9): ")) - 1
        
        # Update the board
        if board[position] == " ":
            board[position] = current_player
            print_board()
        else:
            print("Invalid move! Try again.")
    
    # Game over
    if " " not in board:
        print("It's a tie!")
    else:
        winner = "X" if board.count("X") > board.count("O") else "O"
        print("Player", winner, "wins!")

# Play the game
play_game()
