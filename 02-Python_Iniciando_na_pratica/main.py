import getpass

print("")
print("********************************************************")
print("******************* Caixa Eletrônico *******************")
print("********************************************************")
print("")

accont_typed = input("Digite sua conta:  ")
password_typed = getpass.getpass("Digite sua Senha:  ")

# accont_list = {
#     '0001-01' : {
#         'password' : '123456',
#         'name' : 'José Malcher Jr',
#         'value': 0
#     },
#     '0002-02': {
#         'password': '123',
#         'name': 'Luci Souza',
#         'value': 0
#     }
# }
acconts_list = [
    {
        'agency': '0001-01',
        'password': '123456',
        'name': 'José Malcher Jr',
        'value': 0
    },
    {
        'agency': '0002-02',
        'password': '123',
        'name': 'Luci Souza',
        'value': 0
    }
]
#
#if accont_typed in accont_list and password_typed == accont_list[accont_typed]['password']:
#     print('Conta Valida')
#     print(accont_typed)
#     # print(password_typed)
# else:
#     print('Conta INVALIDA!')

flag = False
for account in acconts_list:
    if accont_typed == account['agency'] and password_typed == account['password']:
        flag = True
        print("Conta Válida")
        print(accont_typed)
if not flag:
    print("CONTA INVALIDA!")