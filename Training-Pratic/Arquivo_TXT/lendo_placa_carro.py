#Lendo a lista com os arquivos salvos no placa_carro.py

def listar_placas():
    arquivo = open('placa_carro.txt', 'r')
    for placa in arquivo:
        print(placa)
    arquivo.close()


listar_placas()
