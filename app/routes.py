from app.models import User, Deck, match_schema, deck_schema
from app import app
from flask import (
    Blueprint, request, jsonify, render_template, redirect, url_for
    )
from flask_login import current_user, login_user, logout_user
from .models import db


cards = Blueprint('cards', __name__, url_prefix='/cards')
user = Blueprint('user', __name__, url_prefix='/user')

deck = Deck()

@app.route('/', methods=['GET'])
def index():
    return jsonify(
        {
            'msg': 'Hello Flask'
        }
    )


# ----------[ Cardgame Routes ]---------- #
# @cards.route('/')
# def cards_index():
#     return 'Cards home'

@cards.route('/get-deck', methods=['GET'])
def get_shuffled_deck():
    deck.build_deck()
    deck.shuffle_cards()
    output = deck_schema.dump(deck)
    return jsonify(output)

@cards.route('/blackjack/deal', methods=['GET'])
def post_blackjack():
    hand = []
    deck.build_deck()
    deck.shuffle_cards()
    for _ in range(2):
        hand.append(deck.deck_of_cards.pop())
    output = deck_schema.dump(hand)
    print(deck.deck_of_cards)
    print(hand)
    return jsonify(output)

@cards.route('/blackjack', methods=['PUT'])
def put_blackjack():
    return 'Blackjack PUT'

@cards.route('/blackjack', methods=['DELETE'])
def delete_blackjack():
    return 'Blackjack DELETE'


# ----------[ User Routes ]---------- #
@user.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/cards')

    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user is not None and user.check_pw(request.form['password']):
            login_user(user)
            return redirect('/cards')

    return render_template('user/login.html')


@user.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/cards')

    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('user.login'))

        new_user = User(email=email, username=username)
        new_user.set_pw(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/user/login')
    
    return render_template('user/register.html')

@user.route('/logout')
def logout():
    logout_user()
    return render_template('user/logout.html')
