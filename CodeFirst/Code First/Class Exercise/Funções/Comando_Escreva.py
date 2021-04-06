def write(message):
    tam = len(message) + 4
    print('-' * tam)
    print(f'  {message}')
    print('-' * tam)


write('Hello! I am new here')