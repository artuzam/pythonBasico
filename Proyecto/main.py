import Deck
import Hand as H
import utils

deck = Deck.Deck()
deck.shuffle()

# crear manos (listas) vacías de jugador y casa
playerhand = H.Hand('Jugador 1')
dealerhand = H.Hand('Dealer')
# reparte dos cartas al jugador
playerhand.add_new_card(deck.deal())
playerhand.add_new_card(deck.deal())
playerhand.print_hand()
print(playerhand.value)
print('===============================>')
# reparte dos cartas a la casa
dealerhand.add_new_card(deck.deal())
dealerhand.add_new_card(deck.deal())
dealerhand.print_hand(True)
print(dealerhand.value)
