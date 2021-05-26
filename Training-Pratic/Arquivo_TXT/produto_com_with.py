from pprint import pprint

dicionario = {'nome':'', 'descricao':'', 'preco':''}


def cadastro_produto(nome, descricao, preco):
    with open('comercio.csv', 'a') as arquivo:
        arquivo.write(f'{nome};{descricao};{preco} \n')


def listar_produto():
    lista = []
    with open('comercio.csv', 'r') as arquivo:
        for produto in arquivo:
            linha_tratada = produto.strip()
            dados = linha_tratada.split(';')
            produto = {'nome': dados[0], 'descricao':dados[1], 'preco':dados[2]}
            lista.append(produto)
            
    return lista

nome = input('Digite o nome do produto: ')
descricao =  input('Digite a descrição do produto: ')
preco = float(input('Digite o preço do produto: '))

cadastro_produto(nome, descricao, preco)

pprint(listar_produto())



