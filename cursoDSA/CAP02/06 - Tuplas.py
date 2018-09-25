################
#              #
#   TUPLAS     #
#              #
################

# Criando uma tupla em Python
tupla1 = ("Geografia",23,"Elefantes")

# Imprimindo o valor
print(tupla1)

# Tuplas nao suportam append
tupla1.append("Chocolate")

# Tuplas nao suportam delete de um item especifico
del tupla1["Geografia"]

# Tuplas podem ter um unico item
tupla1 = ("Chocolate")

tupla1[0]

#  Verificando o comprimento de uma Tupla
len(tupla1)

# Slicing da mesma forma que se faz com listas
tupla1[1:]

# Cospe o index do elefantes
tupla1.index("Elefantes")

# Tuplas nao suportam atribuicao de item
tupla1[0] = 21

# Deletado a tupla
del tupla1

# Criando uma tupla
t2 = ('A','B','C')

# Usando a funcao list() para converter uma tupla para lista
lista_t2 = list(t2)

lista_t2.append('D')

# Usando a funcao tuple() para converter uma lista em tupla

t3 = tuple(lista_t2)


