import random

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"    

class Deck:
    def __init__(self):
        self.cards = []
        suits  = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
                {'rank' : 'A', 'value' : 11},
                {'rank' : '2', 'value' : 1},
                {'rank' : '3', 'value' : 2},
                {'rank' : '4', 'value' : 3},
                {'rank' : '5', 'value' : 4},
                {'rank' : '6', 'value' : 5},
                {'rank' : '7', 'value' : 6},
                {'rank' : '8', 'value' : 8},
                {'rank' : '9', 'value' : 9},
                {'rank' : '10', 'value' : 10},
                {'rank' : 'J', 'value' : 10},
                {'rank' : 'Q', 'value' : 10},
                {'rank' : 'K', 'value' : 10},
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_delt = [] 
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_delt.append(card)
        return cards_delt
    
class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, cardlist):
        self.cards.extend(cardlist)


    
deck1 = Deck()
deck1.shuffle()

hand = Hand()
hand.add_card(deck1.deal(2))

print(hand.cards[0], hand.cards[1])



# card1 = Card(deck1.cards[0][1], deck1.cards[0][0])
# print(card1)
#****************************************
# shuffle()
# card = deal(1)[0]
# print(card)
# print(card[1]['value'])
#********************************************
# cards_delt = deal(2)
# card = cards_delt[0]
# rank = card[1]
# if rank == 'A':
#     value = 11
# elif rank == '10' or rank == 'J' or rank == 'Q' or rank == 'K':
#     value = 10
# else:
#     value = rank
# rank_dict = {
#     'rank':rank, 'value':value
# }
# print(card)
# print(rank_dict['rank'])
# print(rank_dict['value'])
