destroyer_location = [5, 1], [5, 2]
player_hits = []
player_misses = []
game_board = ["", "  1  ", "2  ", "3  ", "4  ", "5  "], \
             ["1", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], \
             ["2", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], \
             ["3", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], \
             ["4", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], \
             ["5", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],


def check_shot():
    if player_shot in destroyer_location:
        print("\nWell done you have hit the destroyer!")
        player_hits.append(player_shot)
    else:
        print("\nYour aim is off! You missed!")
        player_misses.append(player_shot)


def update_game_board(board):
    for hit in player_hits:
        board[hit[0]][hit[1]] = "[H]"
    for miss in player_misses:
        board[miss[0]][miss[1]] = "[M]"


def print_game_board(board):
    game_str = ""
    i = 0
    for rows in board:
        for boxes in rows:
            i += 1
            if i == 6:
                game_str = game_str + " " + boxes + "\n"
                i = 0
            else:
                game_str = game_str + " " + boxes
    print(game_str)


print_game_board(game_board)
while len(player_hits) < 2:
    while True:
        player_shot = input("Enter your shot (row, column): ").split()
        for i in range(0, 2):
            player_shot[i] = int(player_shot[i])
        if player_shot in player_hits or player_shot in player_misses:
            print("\nYou have already aimed there! The destroyer isn't moving, I swear!\n")
            continue
        else:
            break
    check_shot()
    update_game_board(game_board)
    print_game_board(game_board)
else:
    print("Nice shooting, that ship is heading for Davy Jones' Locker!")
