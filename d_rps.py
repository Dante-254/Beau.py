import random

def chagua():
  player_choise=input('Rock, Paper, Scissors:\n')
  choises=['Rock', 'Paper', 'Scissors']
  computer_choise=random.choice(choises)
  print(player_choise,'\n\n'+computer_choise)

print(chagua())