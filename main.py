import os

def refresh_board(board):
    # Draws the board initially and redraws after move is made
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in range(3):
        for cell in range(3):
            print(f"{board[row][cell]}", end="")
            if cell < 2:
                print(" | ", end="")
            elif cell == 2 and row < 2:
                print(f"\n_ _ _ _ _")


def player_move(board, player):
    # Updates board with players move
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
    winning_combos = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for winner in winning_combos:
        x_count = 0
        o_count = 0
        for square in winner:
            x = square[0]
            y = square[1]
            if board[x][y] == "X":
                x_count += 1
            elif board[x][y] == "O":
                o_count += 1

        if x_count == 3 or o_count == 3:
            print(f"\n Player {player} Wins!")
            return True

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
