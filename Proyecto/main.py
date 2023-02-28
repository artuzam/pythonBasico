import Game as G
import utils


def main():
    game = G.Game(['test1', 'test2'])
    game.print_curr_state()
    cont = input('Digite 1 para continuar: ')
    while cont != '1':
        input('Digite 1 para continuar')
    utils.deal_to_players(game.playerhands, game.deck)
    game.print_curr_state()
    utils.deal_to_dealer(game.dealerhand, game.deck)
    game.print_curr_state()


main()
