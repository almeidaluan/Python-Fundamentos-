########################
#                      #
#       Listas         # 
#                      #
########################

#Criando uma Lista
listaDoMercado = ["ovos,farinha,leite,maças"]

#Imprimindo a lista
print(listaDoMercado)

#Criando outra lista
listaDoMercado02 ["ovos","farinha","leite","maças"]

#Imprimindo a lista
print(listaDoMercado02)

#Criando lista
listaGenerica03 = [12,100,"Universidade"]

print(listaGenerica03)

#Atribuindo cada valor da lista em uma variavel

item00 = listaGenerica03[0]
item01 = listaGenerica03[1]
item03 = listaGenerica03[2]

#Imprimindo variaveis
print(item00,item01,item03)

############################
#                          #
# Atualizando item da lista#        
#                          #
############################

#Imprimindo um item da lista
listaDoMercado[2]

#Atualizando um item da lista
listaDoMercado[1] = "baunilha"

#imprimindo lista alterada
listaDoMercado

##############################
#                            #
# Deletando um item da Listas#        
#                            #
##############################

#Out of index. Nao eh possivel deletar um item que nao existe na lista
del listaDoMercado[5]

#Deletando um item especifico da lista
del listaDoMercado[0]

#Imprimindo list alterada
listaDoMercado

###########################
#                         #
# Lista de lista(Aninhada)#       
#                         #
###########################

#Criando uma lista de listas
listas = [[1,2,3],[4,5,6],[7,8,9]]

#Imprimindo a lista
listas

#Atribuindo um item da lista a um varivel
a = listas[0] #[1,2,3]

b = a[0] # 1

list1 = listas[0]

valor_1_0 = list1[0]

valor_2_0 = list1[2]

list2 = listas[2]

list2

valor_2_0 = list[0]


########################
#                      #
# Operacao com listas  # 
#                      #
########################

#Criando uma lista aninhada ( lista de listas )
listasAninhada = [[1,2,3],[2,3,4],[5,6,7]]

print(listasAninhada)

#Atribuindo a variavel "a" o primeiro valor da lista
a = listasAninhada[0][0]

b = listasAninhada[1][2]

c = listasAninhada[2][2] + 10

e = c * listasAninhada[1][1]

########################
#                      #
# Concatenando listas  # 
#                      #
########################

lista_s1 = [34,32,56]

print(lista_s1)

lista_s2 = [21,90,51]

print(lista_s2)

#Concatenando listas

lista_total = lista_s1 + lista_s2

print(lista_total)

########################
#                      #
#   Operdor IN         # 
#                      #
########################

#Criando uma lista
lista_teste_op = [100,2,-5,3.4]

#Veriicando se o valor 10 pertence a lista Retorna um Boolean
print(10 in lista_teste_op)

#Verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)

########################
#                      #
#   Funçoes Built-in   # 
#                      #
########################

#Funçao len() retorna o comprimento da lista

len(lista_teste_op)

#Funçao max() retorna o valor maximo de lista

max(lista_teste_op)

#Funcao min() retorna o valor minimo da lista

min(lista_teste_op)

#Criando uma lista

novaLista = ["Pamonha","Farofa","Ervilha"]

#Adicionando um item na lista

novaLista.append("Frango")
novaLista.append("Frango")

#Verifica quntas vezes se repete determinado item

novaLista.count("carne")

#Criando uma lista vazia

listaVazia = []

type(listaVazia)

listaVazia.append(50)

old_list = [1,2,3,4]

#Copiando itens de um lista para outra

for item in old_list:
    listaVazia.append(item)

cidades = ["Recife","Manaus","Salvador"]

cidades.extend(["Fortaleza","Palmas"])

cidades.index('Salvador')

cidades.index("Rio de Janeiro") #Rio de janeiro is not in list

cidades.insert(2,110)

#Remove um item da lista

cidades.remove(110)

#Reverte a lista

cidades.reverse()

#Imprimindo  a lista

cidades

x = [2,1,3,5,0]

#Ordena a lista
x.sort()


########################
#                      #
#      Fim             # 
#                      #
########################





