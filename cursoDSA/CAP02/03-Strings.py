####################
#                  #
#   Strings        #
#                  #
####################

Criando um String

#Uma unica palavra
'oi'

#Uma frase
'Criando um string em Python'

#Podemos usar aspas duplas
"Podemos usar aspas duplas ou simples para strings em Python"

#Voce pode combinar aspas duplas e triplas
"Testando Strings em 'Python'"


#######################
#                     #
# Imprimindo Strings  #     
#                     #
#######################

print( 'Testando Strings em Python' )

print( 'Testando \nStrings \nem \nPython' )

print ( '\n' )

####################
#                  #
#Indexando Strings #
#                  #
####################

#Atribuindo uma string
s = 'Data science Academy'

print( s )

#Primeiro elemento da string

s[0]

s[1]

s[2]

Podemos usar um : para executar um slicing que faz a leitura de tudo até um ponto designado.Por exemplo

#Retorna todos os elementos da String,comecando pela posição até o fim da String
s[1:]


#Retorna tudo até a posição 3
s[:3]

#Retorna a string normal
s[:]

#Nós podemos tambem usar a indexação negativa e ler de tras para frente
s[:-1]


Nós tambem podemos usar a notação de indice e fatiar a String em pedaços especificos
(O padrao é 1) Por exemplo, podemos usar dois pontos duas vezes em uma linha
e, em seguida, um numero que especifica a frequencia para retornar elementos.
Por exemplo

s[::1]

s[::2]

s[::-1]


##########################
#                        #
#   Propriedades Strings #
#                        #
##########################

s

#Alterando um caracter

s[0] = 'x'

TypeError                                 Traceback (most recent call last)
<ipython-input-23-ee939bce5bdb> in <module>()
      1 # Alterando um caracter
----> 2 s[0] = 'x'

TypeError: 'str' object does not support item assignment

#Concatenando Strings
s + 'é a melhor maneira de estar preparado para o mercado de trabalho em ciencia de dados!'

s = s + 'é a melhor maneira de estar preparado para o mercado de trabalho em ciencia de dados!'

#Podemos usar o simbolo de multiplicação para criar repetição
letra = 'w'

letra * 3

################################
#                              #
#   Funcoes Built-in de Strings#
#                              #
################################

#Upper Case
s.upper()

#Lower Case
s.lower()

#Dividir uma string por espaços em branco(Padrao)
s.split()

#Dividir uma string por um elemento especifico
s.split(y)


##########################
#                        #
#   Funçoes Strings      #
#                        #
##########################

s = 'seja bem vindo ao universo de Python'

#Deixa a primeira letra da frase maiuscula
s.capitalize()

#Conta o numero de "a" da frase
s.count('a)

#Retorna a posição de determinada letra
s.find('p')

#
s.center(20,'z')

s.isalnum()

s.isalpha()

s.islower()

s.isspace()

s.endswith('o')

s.partition('!')

##########################
#                        #
#   Comparando Strings   #
#                        #
##########################

print( "Python" == "R")

print ( "Python" == "Python")








