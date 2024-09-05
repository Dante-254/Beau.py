import random

cards = []
suits  = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
 
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_delt = [] 
    for x in range(number):
        card = cards.pop()
        cards_delt.append(card)
    return cards_delt

shuffle()

cards_delt = deal(2)
card = cards_delt[0]
rank = card[1]
if rank == 'A':
    value = 11
elif rank == '10' or rank == 'J' or rank == 'Q' or rank == 'K':
    value = 10
else:
    value = rank
rank_dict = {
    'rank':rank, 'value':value
}
print(card)
print(rank_dict['rank'])
print(rank_dict['value'])
