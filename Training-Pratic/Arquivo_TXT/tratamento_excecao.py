#   Criar uma função para salvar instrumentos musicais
#   instrumento = nome, descrição, valor
#   os dados do instrumento serao recebidos por parametro
#   os dados devem ser salvos em arquivo txt
#   cara instrumento deve ser salvo em uma linha
#   os dados devem ser separados por ; (arquivo.csv)
#   usar  tratamento de excecao
#   caso o dado seja salvo com sucesso = "Instrumento salvo com sucesso"
#   caso ocorra erro = "Instrumento nao salvo"

from os import error


def salvar(nome, descricao, valor):
    try:
        with open('instrumento.csv', 'a') as arquivo:
            arquivo.write(f'{nome};{descricao};{valor}\n')
        return 'Instrumento salvo com sucesso!'
    except:
        return 'Instrumento não salvo'

try:
    msg = salvar('corda', 'violao', '90')
    print(msg)
except:
    print('Erro desconhecido :/')
