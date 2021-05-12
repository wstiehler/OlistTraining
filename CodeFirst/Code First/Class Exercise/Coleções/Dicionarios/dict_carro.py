print('Criando um dicionario para armazenar os dados de um carro...')

carro = {
    'marca' : 'Hyndai',
    'modelo' : 'HB20',
    'ano' : 2015,
    'motorização' : 'Automático',
    'acessórios' : [],
    }

print('Dicionarios criado!', carro)
carro['ano'] = 2018
carro['modelo'] = 'Hb20 R-Spec'
print('Troquei de carro - comprei um mais novo!', carro)
print('Colocando acessorios no carro:')
carro['acessórios'] = ['alarme']
print('Instalei um alarme novo: ', carro)
carro['acessórios'].append('som')
print('Coloquei um novo som: ', carro)
carro['acessório'][1] = 'som diferente'
print('Troquei o modelo do som: ', carro)