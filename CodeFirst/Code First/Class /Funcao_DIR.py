class num:
    """
    Classe que simula um objeto inteiro
    """
    def __init__(self, numero):
        self.numero = numero

    def __repr__(self):
        return 'Num: {}'.format(self.numero)

    def __add__(self, operador):
        return self.numero + operador
    