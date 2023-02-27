def print_hand(player, hand):
    print(f'La mano de {player} es:\n')
    for card in hand:
        print(card.__str__())
