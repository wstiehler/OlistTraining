from datetime import date, datetime


lista = ['Participante_1', 'Participante_2', 'Participante_3']

#Escrevendo
# def salvar_premiados(premiados, nome_premio):

#     arquivo = open(f'{nome_premio}.txt', 'w')
#     for s in premiados:
#         arquivo.write(f'{s}\n')
#     arquivo.close()

# salvar_premiados()


#Escrevendo com data e hora
data_hora = datetime.now()
arquivo = open(f'{data_hora}.txt', 'w')
arquivo.write('Carro1\n')
arquivo.close()



