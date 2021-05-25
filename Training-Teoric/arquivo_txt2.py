
lista = ['Participante_1', 'Participante_2', 'Participante_3', 'Participante_4']

def lista_arquivo():

    arquivo = open('curso_python.txt', 'w')
    for aluno in lista:
        arquivo.write(f'{aluno}\n')
    arquivo.close()

lista_arquivo()