from IPython.core.display import clear_output


def display_game(game_list):

    print('Here is the game list')
    print(game_list)


def position_choice():
    choice = ''
    while choice not in ['0', '1', '2']:
        choice = input("Pick a position to replace (0,1,2): ")

        if choice not in ['0', '1', '2']:
            clear_output()
            print("Sorry, but you did not choose a valid position (0,1,2)")

    return int(choice)


def replacement_choice(game_list, position):
    user_replacement = input('Type a string to place at the position : ')
    game_list[position] = user_replacement
    return game_list


def gameon_choice():
    choice = ''

    while choice not in ['Y', 'N']:
        choice = input("Would you like to keep playing? Y or N : ")

        if choice not in ['Y', 'N']:
            clear_output()
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    if choice == 'Y':
        return True
    else:
        return False


game_on = True
game_list = [0, 1, 2]

while game_on:
    clear_output()
    display_game(game_list)

    position = position_choice()
    game_list = replacement_choice(game_list, position)

    clear_output()
    display_game(game_list)

    game_on = gameon_choice()