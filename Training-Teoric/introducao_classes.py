
produto = {'nome':'Piano', 'descricao': 'som', 'valor':5000.00}
lista = []

def create(nome, descricao, valor):
    produto['id'] = produto['id'] +1
    produto['nome'] = nome 
    produto['descricao'] = descricao
    produto['valor'] = valor 
    lista.append(produto)

def read():
    for prod in lista:
        print(f"{prod['id']}, {prod['nome']}, {prod['descricao']}, {prod['valor']} ")

def update():
    pass

def delete():
    pass