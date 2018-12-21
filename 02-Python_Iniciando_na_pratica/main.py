import getpass
import os

while True:
    print("")
    print("********************************************************")
    print("******************* Caixa Eletrônico *******************")
    print("********************************************************")
    print("")

    accont_typed = input("Digite sua conta:  ")
    password_typed = getpass.getpass("Digite sua Senha:  ")

    acconts_list = {
        '0001-01': {
            'password': '123456',
            'name': 'José Malcher Jr',
            'value': 100
        },
        '0002-02': {
            'password': '123',
            'name': 'Luci Souza',
            'value': 300
        }
    }

    if accont_typed in acconts_list and password_typed == acconts_list[accont_typed]['password']:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("")
        print("********************************************************")
        print("*******************    Bem Vindo    *******************")
        print("********************************************************")
        print("")
        print(" 1 - SALDO ")
        option_typed = input("Escolha uma das opções acima: ")
        if option_typed == '1':
            # print('Seu saldo é ' + acconts_list[accont_typed]['value'])
            print('Seu saldo é %s' % acconts_list[accont_typed]['value'])

    else:
        print("---- CONTA INVALIDA ---")

    input('Pressione <ENTER> para continuar...') #pause do prgrama

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')