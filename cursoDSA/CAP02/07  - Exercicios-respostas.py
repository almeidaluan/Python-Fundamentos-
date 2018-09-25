# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista = ["cachorro","papagaio","periquito","Gato","Coelho"]
print(lista)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
primeiro = "Primeiro"
segundo = "Segundo"
terceiro = primeiro + " " + segundo

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla1 = (1,2,2,3,4,4,4,5)

tupla1.count(4)


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario_vazio = {}
print(dicionario_vazio)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario_preenchido = {"Nome1":"Luan","Nome2":"Pedro","Nome3":"Rafael"}
print(dicionario_preenchido)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario_preenchido["Nome"] = "Patricia"

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dicionario = {"Nome1":"Luan","Nome2":["Patricia","Rafael"],"Nome3":"Fulano"}
print(dicionario)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista = ["Pipoca",("Sal","Doce"),{"Nome1":"Pedro","Nome2":"Yasmin"},99.98]


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]




