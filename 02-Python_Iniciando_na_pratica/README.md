## Python - Iniciando na prática

Neste curso, ensinaremos como usar os conceitos básicos da linguagem Python, aplicados em um contexto real. Usaremos capturas do teclado, estruturas de repetição, estruturas condicionais, lógica de programação, tudo de forma prática.

<https://www.schoolofnet.com/curso/python/linguagem-python/python-iniciando-na-pratica/>

---

## <a name="indice">Índice</a>

- [Introdução](#parte1)   
- [Codificação de caracteres](#parte2)   
- [Capturar dados do teclado](#parte3)   
- [Capturar dados de forma segura no teclado](#parte4)   
- [Verificando a autenticidade da conta bancária e da senha](#parte5)   
- [Lógica de programação na autenticidade da conta bancária](#parte6)   
- [Mostrar o saldo do correntista](#parte7)   
- [Execução infinita do programa](#parte8)   
- [Limpando tela do console](#parte9)   
- [Operação ternária](#parte10)   
- [Inclusão de cédulas no caixa eletrônico](#parte11)   
- [Iniciando operação de saque](#parte12)   
- [Testando operação de saque](#parte13)   

---

## <a name="parte1">Introdução</a>

- Python v3

- https://www.python.org/

[Voltar ao Índice](#indice)

---

## <a name="parte2">Codificação de caracteres</a>


[Voltar ao Índice](#indice)

---

## <a name="parte3">Capturar dados do teclado</a>

```python
print("")
print("********************************************************")
print("******************* Caixa Eletrônico *******************")
print("********************************************************")
print("")

accont_typed = input("Digite sua conta:  ")
password_typed = input("Digite sua Senha:  ")
print(accont_typed)
print(password_typed)

```

[Voltar ao Índice](#indice)

---

## <a name="parte4">Capturar dados de forma segura no teclado</a>

```python
import getpass

password_typed = getpass.getpass("Digite sua Senha:  ")

print(password_typed)

```

[Voltar ao Índice](#indice)

---

## <a name="parte5">Verificando a autenticidade da conta bancária e da senha</a>

```python
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
```

[Voltar ao Índice](#indice)

---

## <a name="parte6">Lógica de programação na autenticidade da conta bancária</a>

```python
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
```

[Voltar ao Índice](#indice)

---

## <a name="parte7">Mostrar o saldo do correntista</a>

```python
import getpass

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
    print("CONTA INVALIDA!")

```

[Voltar ao Índice](#indice)

---

## <a name="parte8">Execução infinita do programa</a>



[Voltar ao Índice](#indice)

---

## <a name="parte9">Limpando tela do console</a>

```python
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
```

[Voltar ao Índice](#indice)

---

## <a name="parte10">Operação ternária</a>

```python
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')
    os.system('cls' if os.name == 'nt' else 'clear')
```

[Voltar ao Índice](#indice)

---

## <a name="parte11">Inclusão de cédulas no caixa eletrônico</a>

```python
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
```

[Voltar ao Índice](#indice)

---

## <a name="parte12">Iniciando operação de saque</a>


[Voltar ao Índice](#indice)

---

## <a name="parte13">Testando operação de saque</a>

```python
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
```

[Voltar ao Índice](#indice)

---