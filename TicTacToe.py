ANSI_RED = "\u001b[31m" 
ANSI_GREEN = "\u001b[32m"
ANSI_RESET = "\u001b[0m"
debug = True

def format_mark(mark):
    if mark == "X":
        return f"{ANSI_RED}{mark}{ANSI_RESET}"
    elif mark == "O":
        return f"{ANSI_GREEN}{mark}{ANSI_RESET}"
    return mark 



def tic_tac_toe():
    # Initialize the board
    board = [" " for _ in range(9)]

# debug: prefill board for testing
    if debug != False:
        board =  [ "X", " ", "O",
                "O", "O", " ",
                "X", " ", "X" ]
    
    def print_board(board, winning_line=None):
        orientation = None
        if winning_line:
            orientation = winning_orientation(winning_line)

        for row in range(3):
            row_cells = []
            for col in range(3):
                index = row * 3 + col
                cell = get_cell_display(index, board, winning_line, orientation)
                row_cells.append(f" {cell} ")
            print("|".join(row_cells))
            if row < 2:
                print("---+---+---")
  
    def check_winner(mark):
        return find_winning_line(mark) is not None

    def find_winning_line(mark):
        winning_conditions = [
            (0, 1, 2),  # rows
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),  # columns
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),  # diagonals \
            (2, 4, 6)   # diagonals /
        ]

        for condition in winning_conditions:
            if all(board[i] == mark for i in condition):
                return condition

        return None

    def winning_orientation(line):
        if line in [(0, 1, 2), (3, 4, 5), (6, 7, 8)]:
                    return "horizontal"
        if line in [(0, 3, 6), (1, 4, 7), (2, 5, 8)]:
            return "vertical"
        if line == (0, 4, 8):
            return "diagonal_backslash"
        if line == (2, 4, 6):
            return "diagonal_slash"

    def is_board_full():
        # Check if the board is full
        return " " not in board

    def get_cell_display(index, board, winning_line, orientation):
        mark = board[index]

        if not winning_line or index not in winning_line:
            return format_mark(mark)

        # Overlay rules
        if orientation == "horizontal":
            return "━"
        if orientation == "vertical":
            return "┃"
        if orientation == "diagonal_backslash":
            return "\\"
        if orientation == "diagonal_slash":
            return "/"

    def play_game():
        # Main game loop
        current_mark = "X"
        while True:
            print_board(board, winning_line=None)
            print(f"It's {current_mark}'s turn. Enter a position (1-9): ", end="")
            position = int(input()) - 1  # Adjust for 0-indexing

            # Check if the position is valid
            if position < 0 or position >= 9 or board[position] != " ":
                print("Invalid position, please try again.")
                continue

            # Place the mark and check for a win or draw
            board[position] = current_mark
            if check_winner(current_mark):
                print_board(board=board, winning_line=find_winning_line(current_mark))
                print(f"Player {current_mark} wins!")
                break
            if is_board_full():
                print_board(board=board, winning_line=None)
                print("It's a draw!")
                break

            # Switch player
            current_mark = "O" if current_mark == "X" else "X"

    # Start the game
    play_game()
    
    

# Running the game
tic_tac_toe()

