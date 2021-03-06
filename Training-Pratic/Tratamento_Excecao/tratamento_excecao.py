# Crie uma função para listar os instrumentos salvos na atividade anterior
# a função deve converter cada linha em um dicionario
# a funcao deve tratar os caracteres de quebra de linha
# caso ocorra algum erro durante a leitura, a funcao deve exibit a mensagem de erro (exception)

from pprint import pprint

def listar_instrumentos():
    try:
        lista = []
        with open('instrumento.csv', 'w') as arquivo:
            for linha in arquivo:
                linha_tratada = linha.strip()
                instrumento_lista = linha_tratada.split(';')
                instrumento = {'nome':instrumento_lista[0], 'descricao':instrumento_lista[1],'valor':instrumento_lista[2]}
                lista.append(instrumento)
        return lista

    except Exception:
        return 'Você não tem permissão de leitura!'

try: 
    pprint(listar_instrumentos())
except:
    print('Não sei o que aconteceu')