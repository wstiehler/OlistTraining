# Instrução função WITH - fechamento automático do recurso. 

arquivo = open('teste.txt', 'x')
arquivo.write('Teste...')
arquivo.close()


with open('teste.txt', 'x') as arquivo:
    arquivo.write('Teste...')

