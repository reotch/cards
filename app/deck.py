from random import shuffle

deck = {
    'suits': ['Clubs', 'Diamonds', 'Hearts', 'Spades'],
    'cards': {
        1: 'Ace',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }
}

def build_deck(cards, num_decks=1):
    deck_of_cards = []
    deck_num = 1
    while deck_num <= num_decks:
        for suit in cards['suits']:
            for card in cards['cards']:
                deck_of_cards.append(f'{card} of {suit}')
        deck_num += 1
    print(deck_of_cards)
    return deck_of_cards

def shuffle_cards(cards):
    shuffle(cards)
    return cards

# test
full_deck = build_deck(deck)
print('\n')
print(shuffle_cards(full_deck))
