import random

cards = []
suits  = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
 
for suit in suits:
    for rank in ranks:
        cards.append([rank, suit])

def shuffle():
    random.shuffle(cards)

def deal():
    card = cards.pop()
    return card

shuffle() 
cards_delt = deal()
print(cards_delt)