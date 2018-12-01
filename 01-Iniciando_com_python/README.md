
## Iniciando com python

Python tem se tornado uma linguagem cada vez mais popular no mercado, inclusive no de desenvolvimento web. Nesse treinamento, você entenderá os principais pontos para lhe dar a base necessária para desenvolver suas primeiras aplicações

<https://www.schoolofnet.com/curso/python/linguagem-python/iniciando-com-python/>

---

## <a name="indice">Índice</a>

- [Introdução](#parte1)   
- [Instalando python](#parte2)   
- [Meu primeiro programa](#parte3)   
- [Trabalhando com números](#parte4)   
- [Manipulando strings](#parte5)   
- [Brincando com listas](#parte6)   
- [Condicionais](#parte7)   
- [Trabalhando com For](#parte8)   
- [Trabalhando com While](#parte9)   
- [Iniciando com funções](#parte10)   
- [Parametros nomeados e return](#parte11)   
- [Trabalhando com dicionários](#parte12)   
- [Iterando em dicionários](#parte13)   
- [Concluindo](#parte14)   

---

## <a name="parte1">Introdução</a>

- <https://www.python.org/>

#### Introdução

Sejam bem-vindos a mais um conteúdo da School Of Net. Neste módulo falaremos sobre python.

Python tem se tornado uma linguagem cada vez mais popular no mercado, inclusive no de desenvolvimento web. Nesse conteúdo, ensinaremos os principais pontos, para dar a base necessária, para desenvolverem as primeiras aplicações.

Antes de instalarem o python e iniciarmos com o conteúdo, passaremos algumas informações, importantes, a respeito do python. Vejam os tópicos abaixo:

- O que é a linguagem
- Para que serve
- Como é utilizada
- Quais são os casos de uso, para esta linguagem
  
Muitas vezes, quando falamos que desenvolveremos em python, ou que aprenderemos python, muitas pessoas ficam, ligeiramente, intimidadas. Talvez isso ocorra pelo nome da linguagem, mas o ponto é que a maioria das pessoas sentem medo de aprender, pois acham que é uma linguagem extremamente difícil.

Devemos dizer que não é bem assim. O python é uma das linguagens mais fáceis de aprender. A curva de aprendizagem é muito baixa, porque trata-se de uma linguagem muito simples e flexível.

Se vocês já são programadores, de qualquer outra linguagem, e já têm noções de lógicas de programação, vocês acharão os conceitos iniciais do python, extremamente simples. O mais interessante é que a linguagem é muito simples, mas conseguimos fazer coisas muito complexas.

Quando falamos em python, estamos falando em desenvolver programas referentes a scripts. Nós temos um foco muito grande em web, mas conseguimos desenvolver softwares, criar scripts para rodar no servidor, criar software para computação visual, software para web utilizando django, que é um framework para python, entre outras infinitas possibilidades de desenvolvimento. O python é uma linguagem que pode ser utilizada em diversos locais e é muito famosa porque tem muita gente utilizando. Um dos gigantes que utiliza o python é o Google. Existem muitas entrevistas, com os programadores do Google, e eles sempre acabam citando o python.

A grande sacada do python é que, além de rodar muito bem na web e dar a possibilidade de desenvolvermos softwares desktops, ele é muito bom para cálculos científicos. Desta forma, o python consegue rodar programas extremamente complexos e fazer cálculos muito complexos, além de possuir muitas bibliotecas prontas, para estes fins.

Programar em python está longe de ser uma ativadade somente no ramo da web. Apesar do django tornar a criação de um website muito simples.

O nosso próximo passo é aprendermos a instalar e depois aprenderemos a brincar, diretamente, com o interpretador, no console.

Não podemos garantir que este, será o curso mais dinâmico que vocês já viram, porque iremos ensinar fundamentos de uma linguagem. Falaremos desde, somar e subtrair até trabalhar com lista e objetos. Então, na maior parte do tempo, nós não estaremos desenvolvendo softwares ou exemplos muito práticos. Estaremos mostrando como se trabalha com funções, como funciona a identação, como trabalhar com lista, como printar resultados e coisas deste tipo.

De qualquer forma, peguem firme, porque vale muito a pena. Existe muita coisa legal que vocês podem fazer com python.

[Voltar ao Índice](#indice)

---

## <a name="parte2">Instalando python</a>

Iniciaremos o processo de instalação do python. Devemos prestar muita atenção a um detalhe. O python tem duas versões principais e vocês terão que escolher, neste momento.

O python é muito conhecido pela versão 2.7, ou seja, a maioria dos programas e softwares utilizam esta versão e ela continua sendo mantida. Em paralelo, houve um processo muito grande para a criação da versão 3, da linguagem.

Estas versões foram mantidas de forma independentes e a aceitação da versão 3, demorou um pouco para acontecer. Atualmente, já existem muitas pessoas que a utilizam. Concluímos que o python 3 é uma linguagem melhor. No entanto, não há problema em utilizarmos a versão 2.7 da linguagem. Pelo contrário, é mais fácil encontrarmos softwares e bibliotecas na versão 2.7, para nos ajudar nos projetos.

No momento da criação deste conteúdo, as versões disponíveis são: 3.6.0 e 2.7.13. Como podem ver na imagem acima.

O python pode ser rodado em qualquer sistema operacional. Se estiverem utilizando Linux, podem instalar utilizando o comando $ apt-get install python3. Se estiverem utilizando MAC, podem instalar utilizando brew ou utilizando o pacote binário, disponibilizados no site.

Para Windows, podem baixar o instalador direto do site, escolhendo a versão que quiserem trabalhar.

Não existe problema algum em termos as duas versões do python instaladas na máquina, basta configurarmos as variáveis de ambiente, para que consigamos trabalhar com as duas, ao mesmo tempo.

Se vocês não têm nenhuma versão instalada, instale a versão 3, diretamente. Durante a instalação, no Windows, vocês podem marcar uma opção, que configura a variável de ambiente no path.

Caso tenham a versão 2.7 instalada, deverão instalar a versão 3 e configurar a variável de ambiente também, para que consigam executar as duas versões, na mesma máquina. Após a instalação é interessante renomear o arquivo python.exe para python3.exe. Assim, depois de configurada a variável de ambiente, poderemos digitar python para acessar a versão 2.7 e python3 para acessar a versão 3. Isso é indicado para não haver conflitos entre versões.

Para configurarmos as variáveis de ambiente no Windows, basta copiarmos o caminho completo da pasta, em que a instalação do python se encontra, em seguida, clicamos com o botão direito em meu computador e em propriedades. O próximo passo é acessar Configurações avançadas do sistema e depois variáveis de ambiente. Nas variáveis de ambiente encontraremos uma variável chamada path, é nesta que deveremos incluir o caminho da instalação da versão 3 do python. Lembrando que este procedimento é para quem quiser rodar as duas versões na mesma máquina. Caso estejam instalando pela primeira vez, não terão que fazer este procedimento.

Depois da instalação, vocês deverão abrir o console, do sistema operacional, e digitar python. O comando acessará o interpretador do python e mostrará a versão instalada. Caso estejam trabalhando com duas versões, pode ser que precisem digitar python3, para acessar a versão 3.

O que vocês precisam saber é que, utilizaremos o console do sistema operacional, seja ele qual for, e também, utilizaremos a versão 3 do python, para continuar com o conteúdo proposto.

- <https://www.python.org/downloads/>

[Voltar ao Índice](#indice)

---

## <a name="parte3">Meu primeiro programa</a>

Começaremos a colocar a mão na massa a partir de agora. No conteúdo passado, chegamos a abrir o interpretador, no console, para ver a versão do python. Agora, queremos ir mais longe, utilizando esta ferramenta e mostrando o quão poderosa ela é.

No terminal, digitaremos python, para quem instalou pela primeira vez e python3, para quem está com as duas versões instaladas. Desta forma, abriremos o interpretador do python. O importante é que tenham acesso a versão 3.

Um fato importante a ressaltar, do interpretador, é que conseguimos desenvolver um programa inteiro, dentro dele. Isso é muito poderoso, porque podemos utilizar como prova de conceito.

Quando falamos que podemos desenvolver um programa dentro do interpretador, significa que podemos rodar o comando direto e já teremos os resultados.

Vejam um exemplo simples, abaixo:

```python
$ python
Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+ 2
4
>>> 50/2
25.0
>>>
```

Esta é a grande vantagem de trabalharmos com o interpretador do python. Conseguimos testar os seus comandos, importar módulos, testar funções, fazer testes e brincar com a linguagem, de uma forma bem interativa, sem ter que criar arquivo nenhum, se não quisermos.

Podemos criar variáveis e funções e executá-las, diretamente. Falaremos sobre isso, nos módulos futuros. Vocês precisam entender o poder que têm nas mãos, utilizando uma linguagem muito simples.

Muitas vezes, no decorrer deste conteúdo de python, nós estaremos dentro deste interpretador, para fazermos testes e para dar exemplos.

#### Saindo do interpretador

Para finalizar a execução do interpretador, podemos digitar exit() e dar enter ou digitar control + d. Ambas as formas, são capazes de interromper o interpretador do python.

#### Criando arquivo para executar função
Criaremos um arquivo, pelo terminal, com o nome de hello.py.

vim hello.py

Veja o conteúdo do arquivo hello.py:

```python
def say_hello():
    return "Hello World"

print(say_hello())
```

Apenas definimos uma função chamada say_hello, que retorna uma string Hello World, e depois imprimimos esta função. Para executarmos este arquivo, basta digitarmos o comando abaixo, no terminal:

python hello.py

Teremos a string Hello World no terminal, porque o arquivo foi executado e, a função interna, imprime esta string.

O fato de termos utilizado o python3, antes do nome do arquivo, significa que utilizamos o interpretador, mas de forma indireta. Estamos dizendo para o terminal: "Interprete, utilizando o interpretador do python, o arquivo hello.py". E o interpretador é acionado, executa a função interna e retorna o print, no próprio terminal. Este é o processo que está envolvido por trás do comando.

Conclusão
Gostaríamos que vocês pudessem brincar, da mesma forma que nós brincamos, com a linguagem. Façam, pelo menos, estes testes que fizemos, para que possam começar a sentir a linguagem e perceber como é fácil trabalhar com python. O ideal seria que fizessem mais testes e criassem outros arquivos, executando-os da mesma forma.

Assim, com certeza, vocês fixarão melhor o conteúdo.


[Voltar ao Índice](#indice)

---

## <a name="parte4">Trabalhando com números</a>

Agora que vocês já são especialistas no interpretador do python, vamos falar de um assunto muito importante, que são os números. Tentaremos deixar o assunto o menos tedioso possível, porque temos que passar por este conteúdo, independente, se tem ou não, alguma experiência com programação. Se já tem, tenham um pouco de paciência e saibam que é importante passar por este passo, na aprendizagem.

Vale a pena todos lerem, porque existem algumas dicas e regras, específicas do python.

Primeiro, acessaremos o interpretador. Digitem o comando python ou python3, no terminal.

#### Particularidade da divisão

Basicamente, as características, dos números e operações, são muito semelhantes às demais linguagens, mas existe uma particularidade. Vejam os tópicos abaixo:

- Se somarmos ou subtrairmos, um número inteiro com outro número inteiro, teremos o retorno de um número inteiro
- Se somarmos ou subtrairmos, um número inteiro com um número flutuante, teremos o retorno de um número flutuante
- O mesmo vale para a multiplicação. Se multiplicarmos dois inteiros, teremos um resultado inteiro, mas se um dos dois números for flutuante, teremos um resultado flutuante.
- Para a divisão temos uma particularidade.
    - Mesmo que tenhamos a divisão de dois números inteiros, sempre teremos um resultado do tipo flutuante.

Apesar de existir esta particularidade, é possível pegar apenas a parte inteira de uma divisão, caso seja necessário. Basta que alteremos o operador. Vejam exemplo abaixo:

```
>>> 10/5
2.0
>>> 10//5
2
>>> 11/5
2.2
>>> 11//5
2
>>>
```

Em vez de usar o operador convencional de divisão (/), alteramos para (//) e pronto. Desta forma já podemos pegar a parte inteira da divisão. Para pegar o resto da divisão, podemos utilizar o mesmo operador da maioria das linguagens, que é o módulo (%).

Existe também o operador de exponencial. Basta utilizar (**). Vejam o exemplo:

2 ** 3 = 8

O código, acima, é interpretado como sendo 2 elevado ao cubo, que é 8. Seria a mesma coisa que fazer 2 * 2 * 2 = 8.

#### Expressões matemáticas

No python, não podemos utilizar [] nem {}, para executar uma expressão matemática. Podemos substituir, tudo, por parênteses. Desta forma, o python interpretará que, o que estiver dentro dos parênteses, deverá ser executado antes de qualquer outra operação. Vale, também, a regra matemática de que multiplicação e divisão são executadas antes da adição e subtração, caso não haja parênteses. Vejam o exemplo:

```
# Resultado 10
2 + 2 * 4
# Resultado 16
( 2 + 2 ) * 4
```
Vejam que se você não inserir os parênteses o python irá fazer a multiplicação primeiro. No segundo caso ele executou a adição primeiro, e depois a multiplicação.

Se vocês já trabalham com alguma linguagem de programação, isso não deve ser nenhuma novidade. Caso nunca tenham visto, já sabem que devem utilizar os parênteses, para informar a ordem das operações a serem executadas.



[Voltar ao Índice](#indice)

---

## <a name="parte5">Manipulando strings</a>

Para manipular strings utilizaremos, novamente, o interpretador. Tentaremos fazer com que o conteúdo fique o menos entediante possível, assim como no conteúdo anterior. Acreditem, temos que passar por tudo isso, mesmo que seja muito básico, porque a linguagem possui algumas pegadinhas, que podem levá-los ao erro, caso não aprendam da maneira correta.

Programadores que já sabem manipular uma string, tenham paciência e prestem atenção nas particularidades.

#### Strings, função print e \n

Para definirmos uma string, utilizamos aspas duplas ou simples, tanto faz. Qualquer uma que utilizem, terão o mesmo resultado. O que vocês não podem fazer é iniciar com um tipo e terminar com outro, porque o python interpretará como um erro.

Um exemplo em que aspas podem ser mescladas é quando, na string, existe uma aspa simples. Como no nome próprio Levi's, por exemplo.

```
>>> "String com aspas duplas"
'String com aspas duplas'
>>> 'String com aspas simples'
'String com aspas simples'
>>> "Levi's"
"Levi's"
>>>
```

Outra coisa muito interessante é que temos uma função, nativa do python, que é chamada de print. O print imprime um resultado na tela. Podemos rodar o comando abaixo, para ter hello impresso. Já utilizamos esta função, em um exemplo anterior.

print("hello")

Suponham que quisessem imprimir uma palavra, depois pular uma linha e imprimir outra. Basta utilizar o \n para que a função print faça isso.

```
print("Hello\nWesley")
```

Assim, teremos Hello em uma linha e Wesley na outra. O interpretador entende que deve pular uma linha assim que vir o \n. Saibam que somente a função print que interpreta este /n e pula uma linha. Caso vocês atribuam uma string com \n a uma variável e depois imprima esta variável, não terão o mesmo efeito, porque o \n é interpretado como uma string, realmente.

```
>>> print("Hello\nJose")
Hello
Jose
>>> print("Hello\n\nJose")
Hello

Jose
>>> x = "Hello\nJose"
>>> x
'Hello\nJose'
>>> print(x)
Hello
Jose
>>>
```

Vejam na imagem, acima, os exemplos. Quando colocamos duas vezes o \n, o print pulou duas linhas. Quando atribuímos uma string com \n a uma variável e a imprimimos, sem o print, o interpretador não pulou linha. Depois, imprimindo a mesma variável, com o print, ele pulou.

Fizemos isso só para mostrarmos que somente o print interpreta o \n, como uma quebra de linha, no python. Suponha que exista, realmente, uma situação que o \n faça parte da string e vocês não queiram que o print pule a linha. Existe uma forma de forçar o print a não interpretar o \n como uma quebra. Vejam abaixo:

```
>>> print("c:\number")
c:
umber
>>> print(r"c:\number")
c:\number
```

Basta colocar a letra r, antes da string, desta forma a função print irá interpretar somente como string e não pulará linha.

#### Concatenando strings

```
name = "Wesley"
last_name = "Silva"
name + " " + last_name
```

O símbolo responsável por concatenar é o da adição(+), assim como na linguagem javascript.

O código, acima, nos retornará Wesley Silva, porque concatenamos também o espaço, em forma de string. Caso concatenem apenas as variáveis, não teremos o espaço interno, mas sim WesleySilva. Façam esse teste no interpretador.

#### Multiplicando strings

No python é possível multiplicar até strings. Vejam o código abaixo:

```
name = "Wesley"
last_name = "Silva"
(name + " " + last_name) * 2
```

Assim, teremos o seguinte resultado: Wesley SilvaWesley Silva.

#### Slice

```
>>> name = "Jose Malcher"
>>> name[0]
'J'
>>> name[1]
'o'
>>> name[2]
's'
>>> name[3]
'e'
>>> name[0:3]
'Jos'
>>> name[0:4]
'Jose'
>>> name[4:9]
' Malc'
>>> name[2:9]
'se Malc'
>>>
```

Vejam, na imagem acima, os comandos que são possíveis com o slice. Notem que, sempre o primeiro número é o índice de referência inicial e o segundo, a referência final. Vale lembrar que, os índices sempre começam em 0.

Quando colocamos name[0:4] queremos pegar os elementos de 0 ao 4. Na verdade o primeiro parâmetro só é necessário quando estamos querendo pegar elementos internos. Observem que, se quisermos pegar do 0 ao 4 não precisamos colocar o 0, podemos fazer desta forma: name[:4]. A linguagem já entenderá que estamos tomando, como referência, o início da string, e o mesmo se aplica quando queremos pegar os elementos até o último item, não precisamos informar o último elemento, basta fazermos desta forma: name[4:]. Assim, estamos pegando os elementos do índice 4 até o final, independente de quantos sejam estes elementos.

O conceito do slice é muito utilizado no python, não somente em strings, mas quando queremos fazer paginação ou quando fazemos uma busca no banco de dados e queremos listar elementos de tal a tal. Brinquem com os exemplos deste módulo, porque ele realmente é muito importante. Façam muitos testes, até fixarem os conceitos.

[Voltar ao Índice](#indice)

---

## <a name="parte6">Brincando com listas</a>

Falaremos de outro tipo de dado que podemos trabalhar com python. Este módulo será sobre listas.

As aplicações desenvolvidas com python, utilizam listas a todo momento. Logo, este assunto é muito importante.

Existem listas de clientes, listas de resultados e muitos outros tipos de lista. Ensinaremos a trabalharem com estas listas.

O primeiro detalhe, que precisam saber é que, as listas recebem qualquer tipo de dado dentro dela. Não precisa ser só string, flutuante ou inteiro. Podemos ter todos os tipos de dados dentro de uma mesma lista.

#### Declarando listas

numbers = [0, 2, 4, 6] | numbers2=[10, 12, 14, 16]

#### Concatenando listas

numbers + numbers2

#### Slice em listas

Podemos utilizar o método slice, da mesma forma que utilizamos com strings. Em vez de caracteres, temos elementos independentes. Vejam a imagem, abaixo:

```
>>> numbers = [0,2,4,6]
>>> numbers2 = [10,20,30]
>>> numbers + numbers2
[0, 2, 4, 6, 10, 20, 30]
>>> numbers[0]
0
>>> numbers[:4]
[0, 2, 4, 6]
>>>
```

Da mesma forma que as strings possuem índices, as listas também os possuem. Por isso o slice funciona da mesma forma, para os dois tipos de dados.

Vamos supor uma lista com vários tipos de dados, inclusive uma lista dentro desta outra lista. Vejam como trabalhar com este tipo de situação:

```
>>> mix = [1,4,"5",6.3,[1,2,3]]
>>> mix
[1, 4, '5', 6.3, [1, 2, 3]]
>>> #acessando elemento 4 da lista
...
>>> mix[4][2]
3
>>>
```

Vejam que basta controlar os índices, para chegarmos até o elemento que desejamos acessar.

#### Listas mutáveis

Falar que uma lista é mutável, significa que ela pode sofrer alterações. Em uma lista, já criada, podemos adicionar ou remover elementos. Vejam no exemplo, abaixo:

```
>>> numbers
[0, 2, 4, 6]
>>> numbers.append(8)
>>> numbers
[0, 2, 4, 6, 8]
>>> numbers.remove(8)
>>> numbers
[0, 2, 4, 6]
>>> numbers.append(8)
>>> numbers.append(8)
>>> numbers
[0, 2, 4, 6, 8, 8]
>>> numbers.remove(8)
>>> numbers
[0, 2, 4, 6, 8]
>>> del(numbers[4])
>>> numbers
[0, 2, 4, 6]
>>> del(numbers[1])
>>> numbers
[0, 4, 6]
>>>
```

Para adicionar um elemento a uma lista, utilizamos o comando append().

Para remover elementos de uma lista, existem duas formas. Prestem muita atenção, para não confundirem.

remove - remove(8) - Remove o elemento pelo valor, apagando apenas a primeira ocorrência encontrada

del - del(numbers[4]) - Remove o elemento, de acordo com seu índice

A principal diferença entre del e remove, além da estrutura, é que del apaga por índice e remove apaga por valor. Com o remove corremos o risco de apagar o elemento errado, que tenha o mesmo valor. Com del temos a certeza de estar apagando o elemento, de acordo com o índice. Veja qual se adequa melhor ao projeto que estão trabalhando ou a situação em que se encontram.

Pratiquem bastante este assunto de listas, porque, apesar de ser simples, é muito utilizada, durante a programação com python.



[Voltar ao Índice](#indice)

---

## <a name="parte7">Condicionais</a>

Neste módulo de condicionais sairemos do cenário do interpretador no terminal. Utilizaremos, para exemplificar os testes e o conteúdo, a IDE PyCharm. Vocês podem utilizar outra.

A PyCharm tem duas versões, a Community e a Professional. Para a conclusão do nosso conteúdo a versão community atende todas as necessidades e é gratuita, podem baixar.

Vocês podem fazer o download direto do site da JetBrains: <https://www.jetbrains.com/pycharm/download/.>

Neste módulo, o objetivo não é falar sobre IDE e sim, de condicionais. Começaremos a falar sobre este assunto, que é tão importante para o desenvolvimento de aplicações.

Criaremos um arquivo chamado conditional.py, no mesmo local onde criamos o arquivo hello.py. Neste arquivo inseriremos o conteúdo e os exemplos do assunto atual.

#### If, elif e Else

O if, elif e else são condições existentes para utilizarmos sempre que precisamos fazer uma escolha, em um determinado momento, na aplicação. Quando existem 3 ou mais condições, possíveis, utilizamos todas as condicionais, se forem apenas duas, podemos utilizar o if e o else apenas.

#### Estrutura condicional

```python
total = 101

if total > 100:
    print("Maior que 100")
elif total < 100:
    print("Menor que 100")
else:
    print("falhou")
```


No codigo acima podemos ver o seguinte teste:

1. Testamos se o valor, atribuído à variável total, é maior que 100
2. Testamos se o valor, atribuído à variável total, é menor que 100
3. A terceira e última condicional só vale caso as duas anteriores não forem atendidas. Se trata do else.


Em nosso exemplo, como atribuímos 101, a primeira condição será verdadeira, então teremos a execução do primeiro bloco.

Vocês podem e devem alterar os valores para a variável total, para irem testando. Podem, também, alterar as lógicas das condicionais, para fixarem melhor.

Notem que, em python, nós não utilizamos ponto e vírgula(;) no final de cada linha, nem utilizamos abertura e fechamento de chaves nas estruturas condicionais.

O python trabalha, totalmente, de forma identada. Vocês devem definir um padrão de identação para manter do início até o final do seu projeto. O importante é manter o padrão, para diferenciarem os blocos e condicionais.

if - Primeiro teste de condição, caso seja verdadeiro executa o bloco definido
elif - Testes intermediários a serem feitos, caso o primeiro não seja verdadeiro, podemos ter quantos elif quisermos
else - Última verificação, caso nem a primeira nem as demais condições tenham sido atendidas, caímos no bloco else, que será executado

Vocês podem verificar que o modo de trabalhar com condicionais, no python, é muito simples. Apenas fiquem atentos com a sintaxe que o python trabalha, principalmente se vêm de outras linguagens. Pratiquem bastante, criem novas estruturas condicionais e exemplos, para fixarem o conceito de identação e o NÃO uso de ponto e vírgula nos finais de cada linha.

Depois de tudo feito, acessem a pasta do projeto, pelo terminal, e rodem o comando abaixo, para conferirem os resultados:

python3 conditional.py

Desta forma terão os resultados do arquivo que acabaram de desenvolver as lógicas.

[Voltar ao Índice](#indice)

---

## <a name="parte8">Trabalhando com For</a>

Falaremos sobre o famoso for. A primeira estrutura de repetição com python. O For é muito utilizado durante o processo de desenvolvimento e ajuda a controlar o fluxo da aplicação.

Criaremos um novo arquivo, chamado for.py, somente para não misturar os conteúdos.

#### Estrutura for

```python
lista = [2, 4, 6, 8, 10]

for item in lista:
    print(item)
```

Observem que, primeiro declaramos uma lista e depois percorremos todos os elementos dela, utilizando o loop for. Temos que utilizar a palavra reservada for, depois uma variável, com o nome que quisermos, em seguida outra palavra reservada ine, por último, a lista que queremos percorrer. Podemos, também, passar apenas um fragmento da lista para o for iterar, caso não queiram percorrer a lista completa.

Vejam exemplo abaixo:


```python
lista = [2,4,6,8,10]

for item in lista[1:4]:
    print(item)
```

Desta forma, estamos utilizando o slice, para limitar a iteração. Isso pode ser muito útil em caso de grandes sistemas.

Podemos associar uma condição para imprimir, apenas, os números que forem maiores do que 2. Vejam exemplo abaixo.

```python
lista = [2,4,6,8,10]

for item in lista:
    if item > 2:
        print(item)
```

Vamos conferir os resultados: python for.py

#### Iterando lista de strings com condicionais

Nos exemplos, anteriores, mostramos o loop for apenas com listas numéricas, mas o for é capaz de percorrer qualquer tipo de lista, com qualquer tipo de dados. Vejam, abaixo, um exemplo com uma lista de strings, associada a uma estrutura condicional.

```python
nomes = ["Wesley" , "Silva"]

for nome in nomes:
    if nome == "Wesley":
        print(nome)
```

A condição verifica se o nome é igual a Wesley, caso seja, ele imprime, do contrário ele não faz nada. Deste modo teremos apenas a impressão de Wesley no terminal. Executem o arquivo para terem certeza do resultado.

Podemos fazer o inverso e pegar o que não for igual a Wesley, por exemplo. Basta adicionarmos not, antes da comparação. Vejam o exemplo abaixo:

```python
nomes = ["Wesley" , "Silva" , "Thiago" , "Luis"]

for nome in nomes:
    if not nome == "Wesley":
        print(nome)
```
Aumentamos o número de nomes na lista, para conseguirem ver o teste lógico funcionando, corretamente.

#### Operador de comparação (==)

Ainda não tínhamos falado do operador de comparação ==. Este operador é capaz de comparar se uma string é igual a outra string ou um número igual a um outro número. Notem a diferença entre, 1 sinal de igual (=) e 2 sinais de igual (==).



= Atribuir um valor a alguma variável

== Comparar dois valores

#### Conclusão

É desta forma, bem simples, que trabalhamos com loops no python. Adicionamos, junto com os loops, as condicionais, que já havíamos ensinado.

Assim,, vocês observam como os assuntos se cruzam e como os conceitos são aplicados em projetos reais.

Não deixem de praticar muito, para que o conteúdo seja sempre muito bem fixado.

- 01-Iniciando_com_python\for.py

```python
list = [1,2,3,4,5,6,7,8]

for item in list[2:5]:
    if item > 2:
        print(item)
        #print("Maior que 2")

list2 = ["Jose", "Malcher"]
for name in list2:
    if not name == "Jose":
        print(name)
```

```
3
4
5
Malcher
```

[Voltar ao Índice](#indice)

---

## <a name="parte9">Trabalhando com While</a>

Falaremos sobre a segunda forma de trabalhar com loops, no python.

Da mesma forma que trabalhamos com o for, temos outro tipo de laço de repetição chamado while.

O while é o famoso enquanto. Usando uma explicação mais simples, podemos dizer que: enquanto uma condição estiver sendo verdadeira, ele irá executar uma determinada ação.

Criaremos um novo arquivo chamado while.py.

#### Estrutura while

```python
number = 5

while number < 10:
    print(number)
    number += 1
```

O primeiro passo, para trabalhar com while, é atribuir um valor a uma variável. Esta variável será o nosso contador, durante o laço de repetição. Em nosso exemplo criamos a variável number, que tem um valor inicial de 5.

Em seguida, criamos o laço de repetição que começa testando se number é menor do que 10. Como este teste é verdadeiro ele executa o print, que vem logo abaixo, e soma 1 à nossa variável number. Nós chamamos este ato de incremento.

Incrementada a variável, voltamos ao início do while, que é o teste, e vamos testar novamente. Notem que o number não é mais 5, agora ele vale 6, porque foi incrementado na iteração anterior. Como 6 ainda é menor do que 10 ele executa, novamente, e assim, sucessivamente, até que o number seja igual a 10. Sendo igual a 10, a condição do while não será mais verdadeira e a repetição terá um fim.

Rodem o arquivo no terminal, para verem o resultado.

#### Parando while com break

```python
while number < 10:
    print(number)
    number += 1
    if number == 8:
        print("Break!!!")
        break
```

Neste caso, a estrutura trabalha da mesma forma que a anterior, porém, estamos fazendo um teste condicional, dentro do loop while.

Isso significa que, quando o number for igual a 8, nós iremos imprimir Break!!! e aplicaremos o comando break, que irá interromper o loop, imediatamente.

Desta forma, podemos parar o loop, antes que ele chegue ao seu final.

#### While com condicional else

Este é um recurso muito interessante que podemos utilizar no python. Enquanto uma repetição é executada no while, é porque a condição está sendo verdadeira, mas quando chega ao fim, temos uma resposta negativa. Nós podemos utilizar o else por este motivo. Assim que a condição for falsa, em vez de acabar a iteração e não fazermos nada, podemos rodar algum comando dentro do else. Vejam o exemplo abaixo:

```python
while number < 10:
    print(number)
    number += 1
    #if number == 8:
    #    print("Break!!!")
    #    break
else:
    print("not true anymore")
```

Nós comentamos o código anterior, onde existia o break, porque se o break fosse executado, a condição ainda seria true e o else não teria efeito.

#### Como comentar linhas no python

Comentamos, utilizando hashtag (#) na frente de cada linha. Existe outra forma de comentar pedaços de código que é utilizando (''' '''). O código que quiserem comentar deverá estar entre esta sintaxe. O # é utilizado para comentar apenas uma linha, enquanto a outra, comenta um conjunto de linhas. Vejam exemplos de comentários.

```python
#if number == 8:
 #    print("Break!!!")
 #    break

 '''
 if number == 8:
     print("Break!!!")
     break
 '''
```

Façam todos estes testes e criem mais alguns. Nunca fiquem apenas nos exemplos que passamos. Lembrem-se que isso será muito bom para vocês e seus estudos.


```python
number = 2

while number < 10:
    print(number)
    number += 1
    '''
    if number == 8:
        print("Break!!!")
        break
    '''
else:
    print("not true anymore")

```

```
2
3
4
5
6
7
8
9
not true anymore
```

[Voltar ao Índice](#indice)

---

## <a name="parte10">Iniciando com funções</a>

Chegamos em um ponto muito interessante do curso, onde trabalharemos com funções. Função é uma funcionalidade onde podemos ter um agrupamento de código ou comandos, que podem ser executados quantas vezes forem necessárias.

Com funções, conseguimos otimizar tarefas e ganhar tempo de desenvolvimento. Suponham que exista uma tarefa que executem muitas vezes em todos os seus projetos. Neste caso, ao invés de ficar criando código para esta tarefa, em todos os projetos, vocês podem criar uma função que resolva este problema. Uma vez que a função está criada, basta fazer a chamada da mesma e o código será executado.

Criem outro arquivo chamado functions.py e sigam os exemplos abaixo.

#### Estrutura de uma função simples

Para criarmos uma função, sempre precisamos definí-la. O python trabalha com esta forma de definição. Vejam o exemplo abaixo:

```python
def call_numbers():
    for number in range(0,10):
        print(number)

call_numbers(
```

Notem que, primeiro usamos a palavra reservada def. Em seguida, colocamos o nome da função que queremos criar. Tudo que estiver identado, abaixo desta função, fará parte dela.

Geramos um loop for, dentro da função que vai iterar uma lista numérica de 0 a 10. Para criarmos esta lista, utilizamos uma função chamada range. E por último, imprimimos os números.

Observem que, se nós não tivéssemos chamado a função, na última linha, nada teria acontecido. Isso ocorre porque, uma função sempre deve ser chamada, caso contrário, ela não tem efeito algum.

#### Função com parâmetros

```python
def call_numbers_with_limit(limit):
    list = range(0,10);
    for number in list[0:limit]:
        print(number)

call_numbers_with_limit(5)
```

Notem que, desta vez, estamos passando um parâmetro, dentro dos parênteses da função. Este valor pode ser utilizado, dentro da função, da maneira que acharem necessário. Em nosso exemplo, ele serve de limitador para a iteração do loop for.

Primeiro, nós geramos a lista, normalmente, utilizando a função range. Em seguida, fizemos o loop for, mas não iteramos a lista completa. Estamos utilizando o slice para definir qual será o fragmento da lista que iremos percorrer, e o mais interessante é que este valor foi passado por parâmetro. Desta forma, podemos chamar a função e alterar, somente o parâmetro, porque a lógica já está formada dentro dela.

Outra forma de utilizar o limit:

```python
def call_numbers_with_limit(limit):
    for number in range(0,limit):
        print(number)

call_numbers_with_limit(50)
```

Neste último exemplo, utilizamos um valor alto de parâmetro, para vocês observarem o poder que temos em uma função. Com apenas uma chamada e passando um parâmetro, nós imprimimos 50 números. Da mesma forma, poderíamos imprimir 1000 ou mais. As funções são ferramentas maravilhosas e com um poder incrível, na programação. Elas podem salvar sua vida e, como já foi dito, não há limite de uso. Podem chamá-la, sempre que for necessário.

Claro que utilizamos um exemplo muito simples. Imaginem que tenham uma função que converta data ou moeda, ou funções que calculem o IMC (Índice de Massa Corporal) de uma pessoa. Basta chamar a função, passando os dados da pessoa, como parâmetro, e a função irá calcular e retornar.

No próximo módulo mostraremos como é possível trabalhar melhor com os parâmetros, pois o python tem um diferencial que permite trabalhar com parâmetros de forma nomeada.


[Voltar ao Índice](#indice)

---

## <a name="parte11">Parametros nomeados e return</a>

Manteremos os exemplos anteriores e entenderemos melhor, o funcionamento das funções. Trabalharemos com parâmetros nomeados, o que é um super diferencial do python.

Na maioria das linguagens de programação, quando chamamos uma função, passamos o parâmetro, diretamente, como foi feito no último exemplo, do módulo anterior.

Vejam um exemplo de uma função com mais de um parâmetro:

```python
def call_numbers_with_limit(limit , limit2 , limit3):
    for number in range(0,limit):
        print(number)

call_numbers_with_limit(50 , 1 , 10)
```

Observem que, temos 3 parâmetros declarados na função acima. Na chamada, também, passamos os 3 parâmetros que a função exige. Como são poucos parâmetros, é possível controlarmos e sabermos que estão na ordem correta.

Suponham uma função com muitos parâmetros e onde, talvez, nós não saibamos qual a ordem deles. Para não corrermos o risco de confundirmos e errarmos, o python disponibiliza este recurso maravilhoso de parâmetros nomeados.

#### Criando exemplo calculadora para parâmetros nomeados

```python
def calculator(x,y):
    print(x-y)

calculator(10,5)
```

Nós sabemos que, na matemática, dependendo a operação, a ordem dos fatores podem alterar o resultado. No exemplo, acima, se fizermos 10 - 5 teremos o resultado igual a 5, mas se fizermos o contrário, teremos -5, como resultado.

Para evitar erros de ordens, o python oferece a possibilidade de nomear os parâmetros, na hora de chamar a função. Vejam o exemplo abaixo:

```python
def calculator(x,y):
    print(x-y)

calculator(y=5,x=10)
```

Colocamos o nome do parâmetro e igualamos ao valor que queremos informar. Desta forma, podemos colocar em qualquer ordem, que o python saberá tratar e executar a função, corretamente. Isso é maravilhoso e muito prático, quando estamos falando de funções que possuem muitos parâmetros.

#### Informando valores padrões para parâmetros

Existe, também, a possibilidade de informarmos valores padrões, para as variáveis. Significa que, se o usuário não informar valor nenhum, a função pegará um valor pré-determinado, na declaração da função. Vejam o exemplo:

```python
def calculator(x=10,y=5):
    print(x-y)

# Resultado com valores padrões = 5
calculator();

# Passando valor apenas para x | Resultado = 15
calculator(20);

# Passando valor apenas para y | Resultado = 0
calculator(y=10);
```

#### Utilizando return nas funções

Por enquanto, nossos exemplos de funções, apenas, imprimiram algo. Nós podemos querer que uma função, apenas, atribua um valor a uma variável, por exemplo. Neste caso, podemos utilizar o return, que interrompe a função e retorna o valor que nós definirmos. Vejam exemplo:

```python
def calculator(x=10,y=5):
    return x-y

result = calculator(20,10)
print("Result is ",result)
```

Em vez de imprimir, nós retornamos o valor da função, atribuindo à variável result. Desta forma, podemos utilizar a variável result onde quisermos, sabendo que ela contém o resultado de nossa função. Assim, demos um print de uma string, seguida do resultado. Para isso, separamos string e resultado por vírgula, para que a função print não retorne um erro.

[Voltar ao Índice](#indice)

---

## <a name="parte12">Trabalhando com dicionários</a>

Ensinaremos uma outra estrutura de dados que podemos trabalhar com python. Esta estrutura se chama dicionário.

Muitas pessoas acham que o python é parecido com o PHP, que tem o array e que podemos fazer o que quisermos dentro destes arrays. Na realidade, o python trabalha com dicionários e estes dicionários são similares aos arrays associativos do PHP. Um dicionário é sempre composto por chave e valor.

Criem um novo arquivo chamado dict.py, para seguirem os exemplos, ou utilizem o próprio interpretador. Neste caso, achamos mais dinâmico a utilização do interpretador, porque vocês observam os resultados a medida que os elementos são adiconados ao dicionário.

#### Estrutura de um dicionário

```python
cars = {}
```
Assim, temos a declaração de um dicionário, chamado cars, que está em branco, inicialmente. Começaremos a atribuir valores a ele.

```python
cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"
```

Vejam, abaixo, o resultado no interpretador do python:

```
>>> cars = {}
>>> cars
{}
>>> cars["corola"] = "red"
>>> cars["fit"] = "blue"
>>> cars["gol"] = "black"
>>> cars
{'corola': 'red', 'fit': 'blue', 'gol': 'black'}
>>>
```

Trabalhar com dicionários é muito importante. Na verdade, trabalhar com esta estrutura de chave e valor, em qualquer linguagem, é essencial para o controle de dados, de uma aplicação. Deêm atenção especial a este assunto. Vejam mais algumas funcionalidades que os dicionários nos proporcionam.

```
>>> cars.keys()
dict_keys(['corola', 'fit', 'gol'])
>>> cars.values()
dict_values(['red', 'blue', 'black'])
>>> cars["corola"]
'red'
>>>
```

- cars.keys() - Retorna todas as chaves do dicionário
- cars.values() - Retorna todos os valores do dicionário
- cars.["corola"] - Retorna o valor referente a chave informada

Um exemplo que podemos dar, do uso de dicionários, é quando vocês utilizam o Django, que é um framework de python para desenvolvimento web. Utilizando este framework, vocês utilizam dicionários a todo momento, porque vocês precisam criar estas estruturas para conseguirem trabalhar com o fluxo de dados.

#### Outras formas de criar um dicionário

```python
# Declarando um dicionário usando dict
people = dict(Wesley='Father',Mariana="Mother",Sarah="baby")

# Declarando um dicionário com chaves
family = {
    'wesley' : 'Father'
}

# Verificando se existe uma chave antes de imprimir
if 'Wesley' in people:
    print(people['Wesley'])
```

Vejam que, além de criarmos dicionários de formas diferentes, nós mostramos uma forma de verificar se existe uma chave, dentro do dicionário, antes de imprimir. Desta forma, evitamos erros, durante a programação.

#### Conclusão

O que vocês precisam entender é que, dicionários são estruturas com chave e valor. Há a possibilidade de existir um dicionário dentro de outro dicionário.

Outro fato importante que devem ter atenção, é na estruturação dos seus dicionários. Vocês devem estruturar muito bem, para consiguirem trabalhar de forma organizada.

Um exemplo simples que podemos citar é o seguinte:

Suponham que, vocês desenvolverão uma aplicação de pagamento, via cartão. O sistema irá pegar dados de um formulário, preenchido pelo usuário. Neste formulário, o usuário preencherá: nome, endereço, número do cartão, entre outros dados. Depois de receber estes dados, do formulário, vocês deverão configurar um dicionário, com a mesma estrutura que o sistema de pagamento exige.

Desta forma, vocês estão adequando a estrutura de vocês, exatamente, à estrutura exigida pelo sistema de validação do cartão. Sendo assim, terão a aplicação se comunicando, corretamente, com o sistema de pagamento. Isso quer dizer que vocês criam, da maneira que quiserem e na ordem que quiserem, seus dicionários.

Este conceito de biblioteca é muito importante. Estudem bastante e tentem entender todo funcionamento. Criem exemplos e testes próprios, para irem se acostumando com a estrutura e o conceito.





[Voltar ao Índice](#indice)

---

## <a name="parte13">Iterando em dicionários</a>

Para finalizarmos o conteúdo de dicionários, precisamos ensinar a fazer uma iteração nos dicionários. Assim, conseguirão percorrer um dicionário inteiro e trabalhar com a estrutura de dados que ele fornece.

Alguns programadores trabalham da seguinte forma:

```python
cars = {
    "Corola" : "red",
    "Fit" : "green",
    "320" : "black"
}

for car in cars:
    print(car + " - " + cars[car])
```

Isso pode parecer, e na verdade é, uma "gambiarra". Não pode ser normal fazermos uma iteração e dentro, precisarem utilizar o dicionário, novamente, passando as chaves, para resgatar os dados. Mesmo sendo uma gambiarra, não está totalmente errado, porque funciona, corretamente, mas "cheira mal".

Isso ocorre porque a iteração de um dicionário, com o for, só consegue retornar as chaves. Logo, precisamos colocar o dicionário e passar a chave, para conseguirmso pegar o valor, a cada iteração.

#### Forma correta de iterar um dicionário

Antes de falarmos da forma correta, devemos lembrar que mostramos algumas funções, no módulo anterior, que retornam alguns valores, referentes a um dicionário. Falamos sobre cars.keys() e também cars.values(). Com estes métodos, nós conseguimos pegar os valores ou as chaves. Mas e se precisássemos pegar os dois juntos?

Existe um outro método para pegarmos os valores em pares: cars.items(). Sabendo disso, mostraremos a melhor maneira de iterar um dicionário.

```python
cars = {
    "Corola" : "red",
    "Fit" : "green",
    "320" : "black"
}

for key, value in cars.items():
    print(key + " - " + value)
```

Observem as mudanças:

1. Nós passamos dois parâmetros de resgate para a iteração: key e value
2. Como separamos em dois parâmetros de resgate, devemos passar dois parâmetros para a iteração, também. Por isso, passamos cars.items() e não somente cars.
3. Em seguida, para iteração, utilizamos os valores diretos, porque o for nos retornará, corretamente, as chaves e os valores, nas variáveis key e value.
   
Notem que, se fizermos da forma, abaixo, não daria certo:

```python
cars = {
    "Corola" : "red",
    "Fit" : "green",
    "320" : "black"
}

for key, value in cars:
    print(key + " - " + value)
```

Esta estrutura não funciona porque estamos pedindo para o for separar o retorno em dois parâmetros, mas estamos passando um dicionário, que não está configurado em pares, por isso que o for não consegue interpretar. Se passarmos da primeira maneira, o for consegue interpretar, corretamente. Vejam a diferença entre uma forma e a outra:

```python
>>> cars = {}
>>> cars["corola"] = "azul"
>>> cars["GOL"] = "verde"
>>> cars["fit"] = "amarelo"
>>> cars
{'corola': 'azul', 'GOL': 'verde', 'fit': 'amarelo'}
>>> cars.items()
dict_items([('corola', 'azul'), ('GOL', 'verde'), ('fit', 'amarelo')])
>>>
```

Falamos que esta é a forma correta de se iterar um dicionário, porque estamos trabalhando de uma forma muito mais elegante, e que "soa" ser correta. Isso porque, estamos trabalhando com cada elemento, separadamente, key e value. Lembrando que não tem como trabalhar desta forma com listas, porque listas não possuem chaves e valores. Listas possuem, apenas, os valores diretamente.

[Voltar ao Índice](#indice)

---

## <a name="parte14">Concluindo</a>

Chegamos ao final do conteúdo Iniciando com Python. Com o que vocês aprenderam, neste curso, é possível fazerem uma infinidade de coisas e, o mais importante, já é possível trabalharem com python, em aplicações mais simples.

Conseguem, também, interpretar muitos códigos de python, que estão espalhados por aí, porque já conhecem a estrutura das principais funcionalidades da linguagem.

O nosso objetivo foi alcançado, passando os conceitos básicos de Python e fazendo com que o Python não pareça mais uma linguagem estranha ou difícil de se aprender.

Este foi o conteúdo introdutório de Python, esperamos que vocês tenham gostado.

O próximo passo, se gostaram da linguagem, será procurar o nosso conteúdo de Python Orientado a Objetos, onde ensinamos conteúdos mais avançados e exigiremos estes conhecimentos básicos, como pré-requisito.

Neste conteúdo de Python Orientado a Objetos, falamos como trabalhar com módulos, pacotes, classes, atributos, métodos, cálculos, heranças de classes e muitos outros pontos importantes. Separamos os conteúdos para não ficar muito pesado e com muitas informações, podendo gerar confusões.

Vocês já têm o básico de Python. Recomendamos que treinem bastante, refaçam os exemplos e baixem alguns programas, criados em Python, para analisarem e verificarem o que vocês entenderam.

Vocês perceberam o quão fácil e prático é trabalhar com esta linguagem.

Esperamos que, realmente, tenham gostado e aprendido a linguagem Python.

Até o próximo conteúdo.

++ <https://www.schoolofnet.com/canal-direto-ao-ponto/python-dicionarios-vs-listas-vs-tuplas/>

[Voltar ao Índice](#indice)

---
