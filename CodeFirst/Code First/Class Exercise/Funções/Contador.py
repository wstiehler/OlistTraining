from time import sleep


def Contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('=-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}, ', end='', flush=True) #Flush=True serve para contar certinho
            sleep(0.3)
            cont += passo
        print('Fim!')
    else:
        while cont >= fim:
            print(f'{cont}, ', end='', flush=True)
            sleep(0.3)
            cont -= passo
        print('Fim!')


Contador(1, 10, 1)
Contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Informe o inicio: '))
fim = int(input('Informe o fim: '))
pas = int(input('Informe o passo a passo: '))
Contador(ini, fim, pas)