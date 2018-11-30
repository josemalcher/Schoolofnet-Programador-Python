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


[Voltar ao Índice](#indice)

---

## <a name="parte5">Manipulando strings</a>


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
