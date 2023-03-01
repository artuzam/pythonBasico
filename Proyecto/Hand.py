VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Hand:
    def __init__(self, playername):
        self.playername = playername
        self.cardlist = []
        self.value = 0

    def print_hand(self, isdealer=False):
        print(f'La mano de {self.playername} es:')
        for i in range(0, len(self.cardlist)):
            if isdealer and i == 0:
                print('X X')
            else:
                print(self.cardlist[i])
        showvalue = 'X' if isdealer else self.value
        print(f'El valor actual de la mano es: {showvalue}')
        print('**--------------*X*--------------**\n')

    def add_new_card(self, card):
        self.cardlist.append(card)
        self. value += VALUES[card.rank]
