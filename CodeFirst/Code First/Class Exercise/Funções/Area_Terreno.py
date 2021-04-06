def area(largura, comprimento):
    a = larg * comp

    print(f'A área de um terreno {larg} x {comp} é {a} metros quadrados.')


print('Controle de terreno')
print('-' * 20)

larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
