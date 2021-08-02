# from random import shuffle
from app.models import Deck

# class Card:
#     """Creates a single card"""
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value

#     def show_card(self):
#         print(f'{self.value} of {self.suit.title()}')


# class Deck:
#     """Creates deck(s) of cards and shuffles"""
#     def __init__(self, num_decks=1):
#         self.num_decks = num_decks
#         self.cards = []
#         self.suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
#         self.build_deck()

#     def build_deck(self):
#         deck_num = 1
#         while deck_num <= self.num_decks:
#             for suit in self.suits:
#                 for value in range(1, 14):
#                     self.cards.append(Card(suit, value))
#             deck_num = deck_num + 1

#     def shuffle_deck(self):
#         shuffle(self.cards)
#         return self.cards

#     def show_cards(self):
#         for card in self.cards:
#             card.show_card()

#     def draw_card(self):
#         return self.cards.pop()


class Player:
    """One who plays cards"""
    def __init__(self, name='Player'):
        self.name = name
        self.hand = []
        self.cards = 0
        self.score = 0

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show_card()

    def blackjack(self):
        return 'Blackjack!'

    def twenty_one(self):
        return 'You win!'

    def __str__(self):
        return f'Player'

    
class Dealer(Player):
    """One who also deals cards"""
    def __init__(self, name='Dealer'):
        super().__init__(name)

    def deal_hand(self, cls, deck):
        """Deals cards up to the number needed per the game"""
        while(cls.cards < 2):
            cls.hand.append(deck.cards.pop())
            cls.cards += 1
        return cls.hand

    def __str__(self):
        return f'Dealer'


class Game:
    """General game settings"""
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()
        self.gamers = [self.dealer, self.player]


    def get_players(self):
        pass

    def win(self, cls):
        print(f'{cls} wins!')


# class Blackjack(Game):
#     """Rules and play for Blackjack"""
#     def __init__(self):
#         super().__init__()
        

#     def play_blackjack(self):
#         # shuffle deck
#         self.deck.shuffle_deck()
#         # deal a hand to each gamer playing
#         for gamer in self.gamers:
#             self.dealer.deal_hand(gamer, self.deck)
#         self.player.show_hand()
#         self.dealer.show_hand()
    



# deck = Deck()
# deck.shuffle_deck()

# player = Player('Susan')
# player.draw_card(deck)
# player.show_hand()
# dealer = Dealer('Art')
# print(f'{dealer.name} is dealing to {player.name}')
# dealer.deal_hand(player, deck)
# player.show_hand()