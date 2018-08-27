############################
#                          # 
#   Variáveis e Operadores #
#                          #
############################

#Atribuindo o valor 1 à variável var_teste
var_teste = 1

#Imprimindo o valor da variável
print( var_teste )

#Não podemos utilizar uma variável que não foi definida
my_var

ex: Da erro

#----//----#

var_teste = 2

print( var_teste )

type( var_teste )

var_teste = 9.5

type( var_teste )

x = 1

print( x )

############################
#                          # 
#   Declaração Múltipla    #
#                          #
############################

pessoa1, pessoa2, pessoa3 = "Maria", "José", "Tobias"

print( pessoa1 )

print (pessoa2 )

print( pessoa3 )

fruta1 = fruta2 = fruta3 = "Laranja"

print( fruta1 )

print( fruta2 )

print( fruta3 )

x1 = 50

print( x1 )

#Erro porque não pode começar com numero
1x = 50


####################################################################
#                                                                  #
#   Váriaveis atribuidas a outras variáveis e ordem dos operadores #
#                                                                  #                           
####################################################################


largura = 2

altura = 4

area = largura * altura

print ( area )

perimetro = 2 * largura + 2 * altura

print ( perimetro )

#A ordem dos operadores é a mesma seguida da matemática
perimetro = 2 * ( largura + 2 ) * altura

print ( perimetro )


############################
#                          # 
# Operações com variáveis  #
#                          #
############################

idade1 = 25

idade2 = 35

print( idade1 + idade2 )

print( idade1 + idade2 )

print( idade2 * idade1 )

print( idade2 / idade1 )

print( idade2 % idade1 )


#############################
#                           #
# Concatenação de Variáveis #
#                           #
#############################

nome = "Steve"

sobrenome = "Jobs"

fullName = nome + " " + sobrenome

print( fullName )
