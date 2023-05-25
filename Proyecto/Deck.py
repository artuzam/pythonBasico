import Card as C
import random

SUITS = ("\u2764", "\u2666", "\u2660", "\u2618")
RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")


class Deck:
    # inicializa un nuevo deck.
    # recibe suits y ranks
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                # crea una nueva carta y la agrega a la lista
                self.deck.append(C.Card(suit, rank))

    # mezcla la baraja
    def shuffle(self):
        random.shuffle(self.deck)

    # reparte una carta
    def deal(self):
        single_card = self.deck.pop()
        return single_card
