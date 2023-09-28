values = {
    'a1': " ",
    'b1': " ",
    'c1': " ",
    'a2': " ",
    'b2': " ",
    'c2': " ",
    'a3': " ",
    'b3': " ",
    'c3': " ",
}


def ask_to_play():
    answer = input("\nDo you want to play Tic-Tac-Toe?\nEnter 'Y' to play, 'N' to quit: ").lower()
    if answer == "y" or answer == "n":
        if answer == "y":
            return True
        else:
            print("\nGood Bye!")
            return False
    else:
        ask_to_play()


def players_names():
    user_1 = input("\nEnter first player's name: ").title()
    player_1 = ""
    player_2 = ""
    turns_chosen = False
    while not turns_chosen:
        symbol = input(f"{user_1}, choose X or O: ").lower()
        if symbol == "x" or symbol == "o":

            same_name = True
            while same_name:
                user_2 = input("Enter second player's name: ").title()
                if user_2 == user_1:
                    print("Sorry, this is first player's name. Please, choose a different name.")
                    same_name = True
                else:
                    same_name = False

            if symbol == "x":
                player_1 = user_1
                player_2 = user_2
                turns_chosen = True
            else:
                player_2 = user_1
                player_1 = user_2
                turns_chosen = True
        else:
            turns_chosen = False
    return [player_1, player_2]


def print_game(dict):
    game = f"\n     a   b   c  \n   _____________\n1  | {dict['a1']} | {dict['b1']} | {dict['c1']} |\n   _____________\n2  | {dict['a2']} | {dict['b2']} | {dict['c2']} |\n   _____________\n3  | {dict['a3']} | {dict['b3']} | {dict['c3']} |\n   _____________\n"
    print(game)


def play(player, symbol):
    valid_entry = False
    while not valid_entry:
        location = input(f"{player}, enter the cell number (e.g: B2): ").lower()
        try:
            values[location]
        except KeyError:
            print("Oops! Invalid cell name!")
        else:
            if values[location] == " ":
                values[location] = symbol
                print_game(values)
                valid_entry = True
            else:
                print(f"{location} was already used.")


def is_winner(player, entries):
    if (entries["a1"] == entries["b1"] and entries["b1"] == entries["c1"] and entries["c1"] != " ") or \
            (entries["a2"] == entries["b2"] and entries["b2"] == entries["c2"] and entries["c2"] != " ") or \
            (entries["a3"] == entries["b3"] and entries["b3"] == entries["c3"] and entries["c3"] != " ") or \
            (entries["a1"] == entries["a2"] and entries["a2"] == entries["a3"] and entries["a3"] != " ") or \
            (entries["b1"] == entries["b2"] and entries["b2"] == entries["b3"] and entries["b3"] != " ") or \
            (entries["c1"] == entries["c2"] and entries["c2"] == entries["c3"] and entries["c3"] != " ") or \
            (entries["a1"] == entries["b2"] and entries["b2"] == entries["c3"] and entries["c3"] != " ") or \
            (entries["a3"] == entries["b2"] and entries["b2"] == entries["c1"] and entries["c1"] != " "):
        print(f" {player}, you WON!\n")
        return True
    if is_tied(entries):
        return True


def is_tied(values_dict):
    for entry in values_dict:
        if values_dict[entry] == " ":
            return False
        else:
            pass
    print("IT's A TIE!\n")
    return True


##### MAIN PROGRAM #####
game_on = ask_to_play()

while game_on:
    players = players_names()
    print(f"\n{players[0]} is Player-1\n{players[1]} is Player-2")

    game_over = False
    print_game(values)
    while not game_over:
        play(players[0], "X")
        if is_winner(players[0], values):
            game_over = True
        else:
            play(players[1], "O")
            if is_winner(players[1], values):
                game_over = True


    values = {
        'a1': " ",
        'b1': " ",
        'c1': " ",
        'a2': " ",
        'b2': " ",
        'c2': " ",
        'a3': " ",
        'b3': " ",
        'c3': " ",
    }
    ask_to_play()
