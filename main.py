lista = ['Participante_1', 'Participante_2', 'Participante_3']


def arquivos():

    arquivo = open('archive.txt', 'x')
    arquivo.writelines(lista)
    arquivo.close()

