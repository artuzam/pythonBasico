import Deck as D
import Hand as H


class Game:
    def __init__(self, playernames):
        self.gamefinished = False

        # crear nuevo deck
        deck = D.Deck()
        deck.shuffle()

        # reparte dos cartas a la casa
        dealerhand = H.Hand('Dealer')
        dealerhand.add_new_card(deck.deal())
        dealerhand.add_new_card(deck.deal())

        playerhandslist = []
        for player in playernames:
            # reparte dos cartas a cada jugador
            playerhand = H.Hand(player)
            playerhand.add_new_card(deck.deal())
            playerhand.add_new_card(deck.deal())
            playerhandslist.append(playerhand)

        self.deck = deck
        self.dealerhand = dealerhand
        self.playerhands = playerhandslist

    def print_curr_state(self):
        print('ESTADO DE LA PARTIDA')
        self.dealerhand.print_hand(True)
        for hand in self.playerhands:
            hand.print_hand()
