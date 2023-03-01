import fileHandling as fh
import os


def deal_to_players(playerhands, deck):
    os.system('clear')
    for hand in playerhands:
        while True:
            hand.print_hand()
            goon = input(f'{hand.playername}, quiere otra carta? (Y/N): ')
            if goon == 'Y' or goon == 'y':
                os.system('clear')
                hand.add_new_card(deck.deal())
                if hand.value > 21:
                    break
            elif goon == 'N' or goon == 'n':
                os.system('clear')
                break
            else:
                print('Por favor indique Y o N')


def deal_to_dealer(dealerhand, deck):
    os.system('clear')
    while dealerhand.value <= 18:
        dealerhand.add_new_card(deck.deal())
    dealerhand.print_hand(True)


def select_user():
    allusers = fh.get_users()
    if len(allusers) == 0:
        print("No hay usuarios disponibles")
        return create_user()
    else:
        print('Digite el número del usuario que desea')
        for i in range(0, len(allusers)):
            print(f'{i+1}- {allusers[i]}')
    selecteduser = int(input('Número de usuario: ')) - 1

    return allusers[selecteduser]


def create_user():
    allusers = fh.get_users()
    newusername = ''
    while True:
        newusername = input('Ingrese el nombre del nuevo usuario: ')
        if newusername in allusers:
            print('Ese nombre de usuario ya existe')
        else:
            break
    f = open('users.txt', 'a')
    f.write(newusername + '\n')
    f.close()

    return newusername


def handle_user_select():
    selectorcreate = int(
        input('Seleccione una opción.\n 1-Seleccionar usuario\n 2-Crear usuario\n'))
    while True:
        if selectorcreate == 1:
            return select_user()
        elif selectorcreate == 2:
            return create_user()
        else:
            selectorcreate = int(
                input('Seleccione una opción.\n 1-Seleccionar usuario\n 2-Crear usuario\n'))


def declare_winner(game):
    winner = ''
    if game.dealerhand.value == 21:
        return 'DEALER'
    elif game.dealerhand.value < 21:
        diffto21 = 21 - game.dealerhand.value
        for hand in game.playerhands:
            if hand.value == 21:
                return hand.playername
            elif hand.value < 21:
                if 21 - hand.value < diffto21:
                    return hand.playername
    else:
        diffto21 = 0
        for hand in game.playerhands:
            if hand.value == 21:
                return hand.playername
            elif hand.value < 21:
                if 21 - hand.value < diffto21:
                    diffto21 = 21 - hand.value
                    winner = hand.playername
        return winner
