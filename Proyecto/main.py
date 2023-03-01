import Game as G
import utils
import fileHandling as fh
import time
import os


def main():
    username = utils.handle_user_select()
    game = G.Game([username])
    game.print_curr_state()
    # Dialogo de continuar
    cont = input('Desea continuar? (Y): ')
    while True:
        if cont == 'Y' or cont == 'y':
            break
        else:
            print(cont)
            cont = input('Digite Y para continuar: ')
    # Repartir cartas a jugadores
    utils.deal_to_players(game.playerhands, game.deck)
    game.print_curr_state()
    # Repartir cartas al dealer
    os.system('clear')
    print('Repartiendo al dealer...')
    time.sleep(3)
    utils.deal_to_dealer(game.dealerhand, game.deck)
    time.sleep(2)
    os.system('clear')
    game.print_final_state()
    game.winner = utils.declare_winner(game)
    print(f'El ganador es {game.winner.upper()}')
    fh.add_user_stat(username, f'Gano {game.winner}')


main()
