

def refresh_board(board):
    for row in range(3):
        for cell in range(3):
            print(f"{board[row][cell]}", end="")
            if cell < 2:
                print(" | ", end="")
            elif cell == 2 and row < 2:
                print(f"\n_ _ _ _ _")


def player_move(board, player):
    player_pieces = {1: "X", 2: "O"}
    move = int(input(f"\n\nPlayer {player} ({player_pieces[player]}), select square: "))
    column = (move - 1) // 3
    row = move % 3 - 1
    if board[column][row].isnumeric():
        board[column][row] = f"{player_pieces[player]}"
        refresh_board(board)
    else:
        print("Cell already taken")
    return board

def check_win(player, board):
    # Check win logic needs to go in here
    if not board[1][1].isnumeric():                     # Temporarily win when hit middle cell
        print(f"\nGame over! Player {player} wins!")
        return True
    else:
        return False


def main():
    current_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    refresh_board(current_board)
    game_on = True
    current_player = 1
    while game_on:
        current_board = player_move(current_board, current_player)
        if check_win(current_player, current_board):
            game_on = False
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1


if __name__ == "__main__":
    main()
