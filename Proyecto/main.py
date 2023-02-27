import Card
import Deck
import utils
import random

# SUITS = {'corazones':'\u2764', 'diamantes': '\u2666', 'picas': '\u2660', 'Trebol': '\u2618'}
SUITS = ('\u2764', '\u2666', '\u2660', '\u2618')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

deck = Deck.Deck(SUITS, RANKS)
deck.shuffle()

# crear manos (listas) vacías de jugador y casa
player_hand = []
dealer_hand = []
# reparte dos cartas al jugador
player_hand.append(deck.deal())
player_hand.append(deck.deal())
# reparte dos cartas a la casa
dealer_hand.append(deck.deal())
dealer_hand.append(deck.deal())

utils.print_hand('Jugador 1', player_hand)
print('===============================>')
utils.print_hand('Casa', dealer_hand)
