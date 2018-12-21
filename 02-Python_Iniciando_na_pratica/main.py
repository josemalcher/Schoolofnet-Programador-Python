import getpass
print("")
print("********************************************************")
print("******************* Caixa Eletrônico *******************")
print("********************************************************")
print("")

accont_typed = input("Digite sua conta:  ")
password_typed = getpass.getpass("Digite sua Senha:  ")

accont_list = {
    '0001-01' : {
        'password' : '123456',
        'name' : 'José Malcher Jr',
        'value': 0
    },
    '0002-02': {
        'password': '123',
        'name': 'Luci Souza',
        'value': 0
    }
}

if accont_typed in accont_list and password_typed == accont_list[accont_typed]['password'] :
    print('Conta Valida')
    print(accont_typed)
    #print(password_typed)
else:
    print('Conta INVALIDA!')