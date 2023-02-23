import Card as C
import utils

# crea una lista de 4 cartas que representa la mano de un jugador
user_hand = []
for i in range(4):
    new_card = C.Card("bastos", 7, 7)
    user_hand.append(new_card)

# invoca a la función de utils con la lista de Cards creada antes
utils.show_hand(user_hand)
