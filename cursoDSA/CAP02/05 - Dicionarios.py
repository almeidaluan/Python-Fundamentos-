###################
#                 #
# Dicionarios     #
#                 #
###################

#Estrutura Chave - Valor

#Isso eh uma lista

estudantes_list = ["matheus",24,"Fernanda",25,"Tamires",26]

#Isso eh um dicionario

estudantes_dict = {"Matheus":24,"Fernanda":22,"Tamires":26}

print(estudantes_dict)

print(estudantes_dict["Matheus"]) # Retorna o valor associado a chave

estudantes_dict["Pedro"] = 23

print(estudantes_dict["Pedro"])

#Limpa todo o dicionario
estudantes_dict.clear()

#Nao funciona,funciona apenas em listas
del estudantes_dict

#Retorna o tamanho do dicionario
len(estudantes_dict)

#Retorna as chaves 
estudantes_dict.keys()

#Retorna os valores
estudantes.values()

#Me retorna um dicionario separado por tuplas
estudantes_dict.items() #dict_items([('Mateus', 24), ('Fernanda', 22), ('Tamires', 26), ('Cristiano', 25)])

estudantes = {"Maria":27,"Erika":25,"Milton":26}

print(estudantes)

#Atualiza os dicionarios com os valores contidos em outro dicionario
estudantes.update(estudantes_dict)

dict1 = {}

print(dict1)

dict1["key_one"] = 2

print(dict1)

dict1[10] = 5

dict[8.2] = "Python"

#Dicionario de Listas

dict3 = {'key1':1230,'key2':[22,453,73,4],'key3':['leite','maca','batata']}

#Acessando um item da lista,dentro do dicionario
dict3['key3'][0].upper()

#Operacoes com itens da lista,dentro do dicionario

var1 = dict3['key2'][0] - 2

print(var1)

#Duas operacoes no mesmo comando,para atualizar um item dentro da lista
dict3['key2'][0] -= 2

print(dict3)

#Criando dicionarios aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}

dict_aninhado['key1']['key2_aninhado']['key3_aninhado']


