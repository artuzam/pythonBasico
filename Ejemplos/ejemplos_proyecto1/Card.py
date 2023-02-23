'''
Clase Card: representa una carta de naipe
'''


class Card:
    # atributos de instancia de la clase card
    def __init__(self, suit, number, value):
        self.suit = suit
        self.number = number
        self.value = value

    # metodo de la clas
    def print_card(self):
        print(
            f"El numero de la carta el {self.number} y el palo es {self.suit}")
