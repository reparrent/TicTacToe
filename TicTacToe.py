GREEN = "\033[32m"   # X
RED   = "\033[31m"   # O

def tic_tac_toe():
    # Initialize the board
    board = [" " for _ in range(9)]

def print_board(board):
    for row in board:
        for cell in row:
            if cell == "X":
                print(f"{GREEN}{cell}", end=" ")
            elif cell == "O":
                print(f"{RED}{cell}", end=" ")
            else:
                print(cell, end=" ")
        print()

    def check_winner(mark):
        # Check all winning conditions for the given mark
        winning_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                              (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                              (0, 4, 8), (2, 4, 6)]             # diagonals
        for condition in winning_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
                return True
        return False

    def is_board_full():
        # Check if the board is full
        return " " not in board

    def play_game():
        # Main game loop
        current_mark = "X"
        while True:
            print_board(board)
            print(f"It's {current_mark}'s turn. Enter a position (1-9): ", end="")
            position = int(input()) - 1  # Adjust for 0-indexing

            # Check if the position is valid
            if position < 0 or position >= 9 or board[position] != " ":
                print("Invalid position, please try again.")
                continue

            # Place the mark and check for a win or draw
            board[position] = current_mark
            if check_winner(current_mark):
                print_board()
                print(f"Player {current_mark} wins!")
                break
            if is_board_full():
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_mark = "O" if current_mark == "X" else "X"

    # Start the game
    play_game()

# Running the game
tic_tac_toe()
