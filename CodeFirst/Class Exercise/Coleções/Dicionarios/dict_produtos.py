import pprint

produtos = {}

produtos[1] = {
    'descricao' : 'Mouse optico sem fio',
    'preco' : 50.0,
    'estoque' : 130
}

produtos[2] = {
    'descricao' : 'Teclado sem fio',
    'preco' : 100.0,
    'estoque' : 170
}

produtos[3] = {
    'descricao' : 'Monitor 27 pol',
    'preco' : 1000.0,
    'estoque' : 30
}

produtos[4] = {
    'descricao' : 'Caixinhas de som',
    'preco' : 35.0,
    'estoque' : 100
}

#Serve para printar os produtos de uma forma mais legivel. 
pprint.pprint(produtos)

#Serve para printar apenas os registros do produto 1
print(produtos.get(1))

#Serve para printar todos os itens.
print(produtos.items())

#Serve para retornar uma lista contendo todos os valores em um dicionario, sem suas chaves. 
print(produtos.values())

#Serve para retornar uma lista contendo apenas o valor especificado em um dicionario, sem suas chaves. 
print(produtos.get(1).values())

#Serve para limpar todos os itens de um dicionario. 
print(produtos.clear())