def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        raise Exception('Não é possivel dividir por zero!')

try:
    print(dividir(10,2))
except Exception as error:
    print(error)