import requests

BASE = 'http://127.0.0.1:5000/'

deck_response = requests.get(BASE + 'deck')
card_response = requests.get(BASE + 'card')
blackjack_deal = requests.get(BASE + 'blackjack/deal')
print(deck_response.json())
print(card_response.json())
print(blackjack_deal.json())