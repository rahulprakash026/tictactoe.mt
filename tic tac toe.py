def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Enter the row (0, 1, or 2) for {current_player}: "))
        col = int(input(f"Enter the column (0, 1, or 2) for {current_player}: "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    main()
