def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def play_game():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_active = True
    turns = 0

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9, starting from top-left to bottom-right.")

    while game_active:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Space is either taken or out of bounds. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[move] = current_player
        turns += 1

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_active = False
        elif turns == 9:
            print_board(board)
            print("It's a draw!")
            game_active = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()