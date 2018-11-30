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


[Voltar ao Índice](#indice)

---

## <a name="parte7">Condicionais</a>


[Voltar ao Índice](#indice)

---

## <a name="parte8">Trabalhando com For</a>


[Voltar ao Índice](#indice)

---

## <a name="parte9">Trabalhando com While</a>


[Voltar ao Índice](#indice)

---

## <a name="parte10">Iniciando com funções</a>


[Voltar ao Índice](#indice)

---

## <a name="parte11">Parametros nomeados e return</a>


[Voltar ao Índice](#indice)

---

## <a name="parte12">Trabalhando com dicionários</a>


[Voltar ao Índice](#indice)

---

## <a name="parte13">Iterando em dicionários</a>


[Voltar ao Índice](#indice)

---

## <a name="parte14">Concluindo</a>


[Voltar ao Índice](#indice)

---
