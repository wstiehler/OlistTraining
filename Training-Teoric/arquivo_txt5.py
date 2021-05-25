#strip remove espaços em brancos do começo ao final da string e remove os caracteres de escape \t, \n ...

arquivo = open('arquivo_lendo', 'r')
for linha in arquivo:
    linha_tratada = linha.strip()
    print(linha_tratada)
arquivo.close()