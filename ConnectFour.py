def display_board(board):
    print("\t1\t2\t3\t4\t5\t6\t7")
    for r in range(1, len(board)):
        print(r, end="")
        for c in range(1, len(board[r])):
            print(f"\t{board[r][c]}", end="")
        print()


def check_for_win(board):
    # Horizontal
    for r in range(1, 7):
        for c in range(1, 5):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] and board[r][c] != '-':
                return True

    # Vertical
    for r in range(1, 4):
        for c in range(1, 8):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] and board[r][c] != '-':
                return True

    # Diagonal up-right
    for r in range(4, 7):
        for c in range(1, 5):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] and board[r][c] != '-':
                return True

    # Diagonal down-right
    for r in range(1, 4):
        for c in range(1, 5):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] and board[r][c] != '-':
                return True

    return False


def main():
    import sys
    board = [[' ' for _ in range(8)] for _ in range(7)]
    finished = False
    current_player = 'X'

    while not finished:
        # Reset board
        for r in range(1, 7):
            for c in range(1, 8):
                board[r][c] = '-'

        display_board(board)
        game_over = False
        num_moves = 0

        while not game_over:
            valid_input = False

            while not valid_input:
                try:
                    column_chosen = int(input("Enter the column you want to place your piece: "))
                    if column_chosen < 1 or column_chosen > 7 or board[1][column_chosen] != '-':
                        print("Please choose another column!")
                    else:
                        valid_input = True
                except ValueError:
                    print("Please enter a valid column number (1-7)!")

            # Place piece
            for row in range(6, 0, -1):
                if board[row][column_chosen] == '-':
                    board[row][column_chosen] = current_player
                    break

            num_moves += 1
            display_board(board)

            if check_for_win(board):
                print("Congratulations, you won!")
                game_over = True
            elif num_moves == 42:
                print("It was a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

        game_option = input("Type 'Yes' to play again or end the game: ")
        if game_option.strip().lower() != 'yes':
            finished = True
            print("Good Bye!")


if __name__ == "__main__":
    main()
