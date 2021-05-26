
lista = []
dicionario = {'placa':''}


def estacionamento():
    
    dicionario['placa'] = lista.append(input('Digite uma placa: '))

    arquivo = open('placa_carro.txt', 'a')
    arquivo.write(f'{lista} \n')
    arquivo.close()

estacionamento()