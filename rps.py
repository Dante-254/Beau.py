import random

def get_choises():
    player_choise = input('(Rock, Paper, Scissors)\nEnter:')
    options = ['Rock', 'Paper', 'Scissors']
    computer_choise = random.choice(options)
    choises = {'player': player_choise, 'computer': computer_choise}
    return choises

def check_win(player, computer):
    print(f'You chose {player},computer chose {computer}')
    if player == computer:
       return('its a tie')
    elif player == 'Rock':
        if computer == 'Scissors':
            return('Rock smashes Scissors, YOU WIN')
        else:
            return('Paper covers Rock, YOU LOSE')
    elif player == 'Paper':
        if computer == 'Rock':
            return('Paper covers Rock, YOU WIN')
        else:
            return('Scissors cut Paper, YOU LOSE')
    elif player == 'Scissors':
        if computer == 'Paper':
            return('Scissors cut Paper, YOU WIN')
        else:
            return('Rock Smashes Scissors, YOU LOSE')

choises = get_choises()
result = check_win(choises['player'], choises['computer'])
print(result)