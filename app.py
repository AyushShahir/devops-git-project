# Tic-Tac-Toe: Human vs AI

# -----------------------------
# Game Board
# -----------------------------

board = [" " for _ in range(9)]


# -----------------------------
# Display the Board
# -----------------------------

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


# -----------------------------
# Check Winner
# -----------------------------

def check_winner(symbol):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (
            board[position[0]] == symbol
            and board[position[1]] == symbol
            and board[position[2]] == symbol
        ):
            return True

    return False


# -----------------------------
# Check if Board is Full
# -----------------------------

def board_full():
    return " " not in board


# -----------------------------
# AI Turn
# -----------------------------

def ai_turn():

    # 1. Check if AI can win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if check_winner("O"):
                return

            board[i] = " "

    # 2. Check if player can win and block
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if check_winner("X"):
                board[i] = "O"
                return

            board[i] = " "

    # 3. Take the center
    if board[4] == " ":
        board[4] = "O"
        return

    # 4. Take a corner
    corners = [0, 2, 6, 8]

    for i in corners:
        if board[i] == " ":
            board[i] = "O"
            return

    # 5. Take any remaining position
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


# -----------------------------
# Player Turn
# -----------------------------

def player_turn():

    while True:

        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                return

            print("Invalid move! The position is already occupied or out of range.")

        except ValueError:
            print("Please enter a number between 1 and 9.")


# -----------------------------
# Start Game
# -----------------------------

def play_game():

    print("=" * 35)
    print("        TIC-TAC-TOE")
    print("=" * 35)

    print("\nX = You")
    print("O = AI")
    print("\nEnter a number from 1-9 to make your move.")
    print()

    # Show position numbers
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    print("\nLet's start!")
    print("You go first.\n")

    for turn in range(9):

        # Player's turn
        player_turn()
        print_board()

        if check_winner("X"):
            print("🎉 Congratulations! You win!")
            return

        if board_full():
            print("It's a draw!")
            return

        # AI's turn
        print("AI is thinking...")
        ai_turn()
        print_board()

        if check_winner("O"):
            print("🤖 AI Wins! Better luck next time!")
            return

        if board_full():
            print("It's a draw!")
            return


# -----------------------------
# Run the Game
# -----------------------------

if __name__ == "__main__":
    play_game()