import Card
import random


class Deck:
    # inicializa un nuevo deck.
    # recibe suits y ranks
    def __init__(self, suits, ranks):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # crea una nueva carta y la agrega a la lista
                self.deck.append(Card.Card(suit, rank))

    # mezcla la baraja
    def shuffle(self):
        random.shuffle(self.deck)

    # reparte una carta
    def deal(self):
        single_card = self.deck.pop()
        return single_card
