class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representação do objeto fora do escopo da classe
    def __repr__(self):
        return 'Ponto({}, {})'.format(self.x, self.y)


class Linha():
    def __init__(self, p_1, p_2):
        self.ponto_1 = p_1
        self.ponto_2 = p_2

    @property
    def distancia_x(self):
        return abs(self.ponto_2.x - self.ponto_1.x)

    @property
    def distancia_y(self):
        return abs(self.ponto_2.y - self.ponto_1.y)

    def __repr__(self):
        return 'Linha ([{}, {}])'.format(self.ponto_1, self.ponto_2)


ponto_1 = Ponto(5, 2)
ponto_2 = Ponto(1, 5)

#print(ponto_1)
#print(ponto_2)


linha_1 = Linha(ponto_1, ponto_2)
#print(linha_1.distancia_x)
#print(linha_1.distancia_y)
#print(linha_1)

class Quadrado:
    """
    Tentar resolver

    -Herança
    -Usar classe
    """
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

