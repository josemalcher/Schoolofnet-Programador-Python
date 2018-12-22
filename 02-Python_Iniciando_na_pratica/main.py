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
            'value': 100,
            'admin' : False
        },
        '0002-02': {
            'password': '123',
            'name': 'Luci Souza',
            'value': 300,
            'admin': False
        },
        '1111-11': {
            'password': '321',
            'name': 'Administrador Souza',
            'value': 3000,
            'admin': True
        }
    }
    money_slips = {
        '20':  0,
        '50':  0,
        '100': 0,
    }

    if accont_typed in acconts_list and password_typed == acconts_list[accont_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("********************************************************")
        print("*******************    Bem-Vindo    *******************")
        print("********************************************************")
        print("")
        print(" 1 - SALDO ")
        if acconts_list[accont_typed]['admin']:
            print("10 - Incluir cédulas")

        option_typed = input("Escolha uma das opções acima: ")

        if option_typed == '1':
            # print('Seu saldo é ' + acconts_list[accont_typed]['value'])
            print('Seu saldo é %s' % acconts_list[accont_typed]['value'])
        elif option_typed == '10' and acconts_list[accont_typed]['admin']:
            amount_typed = input("Digite a Quantidade de cédulas: ")
            money_bill_typed = input("Digite a célula a ser incluída: ")
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
    else:
        print("---- CONTA INVALIDA ---")

    input('Pressione <ENTER> para continuar...') #pause do prgrama

    os.system('cls' if os.name == 'nt' else 'clear')