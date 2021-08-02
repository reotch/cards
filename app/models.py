import os
from random import shuffle
from datetime import datetime
from app import app, api
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager


# db file location for the server (current directory)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database configs
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cards.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)
# Init LoginManager
login = LoginManager()

# User Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pw_hash = db.Column(db.String(), nullable=False)
    games = db.relationship('Match', backref='player', lazy=True)

    def set_pw(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_pw(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return f'User(\'{self.username}\', \'{self.email}\')'


# Link Flask_Login to db
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Match Classes/Models
class Match(db.Model):
    """A single card game"""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    match_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    winner = db.Column(db.String(80))
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.match_date} between Dealer and {self.player_id}, won by {self.winner}'


# Cards Classes/Models
class Card:
    """Creates a single card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_card(self):
        print(f'{self.value} of {self.suit.title()}')

    def get(self):
        return 

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = {
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
        self.deck_of_cards = []

    def build_deck(self, num_decks=1):
        deck_num = 1
        while deck_num <= num_decks:
            for suit in self.deck['suits']:
                for card in self.deck['cards']:
                    self.deck_of_cards.append(f'{card} of {suit}')
            deck_num += 1
        print(self.deck_of_cards)
        return self.deck_of_cards

    def shuffle_cards(self):
        shuffle(self.deck_of_cards)
        return self.deck_of_cards

# class Deck(Resource):
    # """Creates deck(s) of cards and shuffles"""
    
    # def __init__(self, num_decks=1):
    #     self.num_decks = num_decks
    #     self.cards = []
    #     self.suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
    #     # self.build_deck()

    # def build_deck(self):
    #     deck_num = 1
    #     while deck_num <= self.num_decks:
    #         for suit in self.suits:
    #             for value in range(1, 14):
    #                 self.cards.append(Card(suit, str(value)))
    #         deck_num += 1

    # def shuffle_deck(self):
    #     shuffle(self.cards)
    #     # return self.cards

    # def show_cards(self):
    #     for card in self.cards:
    #         card.show_card()

    # def draw_card(self):
    #     return self.cards.pop()


# Match Schemas
class MatchSchema(ma.Schema):
    class Meta:
        model = Match


# class CardSchema(ma.Schema):
#     class Meta:
#         model = Card

class DeckSchema(ma.Schema):
    class Meta:
        model = Deck
        fields = ('deck_of_cards',)


# Initialize the schemas
match_schema = MatchSchema(many=True)
deck_schema = DeckSchema()

# API resources
# api.add_resource(Card, '/card')
# api.add_resource(Deck, '/deck')