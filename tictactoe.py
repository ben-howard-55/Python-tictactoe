import itertools

# display the board and update the board
def game_board(game_map, player=0, row=0, column=0, just_display=False): 
    try:
        if game_map[row][column] != 0:
            print("location all ready entered: please enter again!")
            return game_map, False

        print("   0  1  2 ")
        if not just_display:
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            print(count, row)

        return game_map, True

    except IndexError as e:
        print("index error bro", e)
        return game_map, False

    except Exception as e:
        print("not good homes", e)
        return game_map, False



# tictactoe win conditions and logic
def win(game_map):
    # horizontal win
    for row in game_map:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is winner horizontally (-)")
            return True


    # vertical win
    for col in range(len(game_map)):
        check = []
        for row in game_map:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is winner vertically (|)")
            return True


    #diagonal win top right to bottom left
    diag = []
    for row, col in enumerate(reversed(range(len(game_map)))):
        diag.append(game_map[row][col])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f"Player {diag[0]} is winner diagonally (/)")
        return True


    #diagonal win top left to bottom right
    diag = []
    for i in range(len(game_map)):
        diag.append(game_map[i][i])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f"Player {diag[0]} is winner diagonally (\\)")
        return True

    return False


play = True
player_choice = itertools.cycle([1, 2])
while play:
    game = [[0, 0, 0,],
            [0, 0, 0,],
            [0, 0, 0,]]
    
    game_won = False
    game, _ = game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_choice)
        played = False
        while not played:
            column_choice = int(input("player select column: "))
            row_choice = int(input("player select row: "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            ask = input("would you like to play again (y/n): ")
            if ask.lower() == "y":
                print("Let's play again!")
            elif ask.lower() == "n":
                print("cya later.")
                play = False
            else:
                print("invalid input, exiting game")
                play = False


