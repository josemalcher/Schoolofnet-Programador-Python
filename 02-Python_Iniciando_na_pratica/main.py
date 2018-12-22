import getpass
import os

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
    '20':  5,
    '50':  5,
    '100': 5,
}

while True:
    print("")
    print("********************************************************")
    print("******************* Caixa Eletrônico *******************")
    print("********************************************************")
    print("")

    accont_typed = input("Digite sua conta:  ")
    password_typed = getpass.getpass("Digite sua Senha:  ")



    if accont_typed in acconts_list and password_typed == acconts_list[accont_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("********************************************************")
        print("*******************    Bem-Vindo    *******************")
        print("********************************************************")
        print("")
        print("1 - SALDO ")
        print("2 - SAQUE")
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
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')
            value_int = int(value_typed)
            money_slips_user = {}

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print('O caixa não tem cédulas disponíveis para este valor')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                print('Pegue as notas:')
                print(money_slips_user)

            # 200 / 100 = 2
            # 200 / 50 = 4
            # 200 / 20 = 10
            #
            # 270 / 100 = 2 - 70
            # 70 / 50 = 1 - 20
            # 20 / 20 = 1 - 0


    else:
        print("---- CONTA INVALIDA ---")

    input('Pressione <ENTER> para continuar...') #pause do prgrama

    os.system('cls' if os.name == 'nt' else 'clear')