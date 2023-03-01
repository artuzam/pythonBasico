import os


def deal_to_players(playerhands, deck):
    os.system('clear')
    for hand in playerhands:
        continues = True
        while continues:
            hand.print_hand()
            goon = input(f'{hand.playername}, quiere otra carta? (Y/N): ')
            if goon == 'Y' or goon == 'y':
                os.system('clear')
                hand.add_new_card(deck.deal())
            elif goon == 'N' or goon == 'n':
                continues = False
                os.system('clear')
            else:
                print('Por favor indique Y o N')


def deal_to_dealer(dealerhand, deck):
    os.system('clear')
    while dealerhand.value <= 18:
        dealerhand.add_new_card(deck.deal())
    dealerhand.print_hand(True)
