class Gatinho:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.mingau_com_fome = False
        self.rodado = 0

    def miar(self):
        if self.mingau_com_fome:
            return 'MIAUUUUUUUUUUU'
        return 'Miau, Miau'

    def andar(self):
        self.rodado +=1
        self.mingau_com_fome = True
        return 'Mingau andando'

    @property
    def velho(self):
        return True if self.idade > 3 else False

    @property
    def cansado(self):
        return True if self.rodado > 5 else False


mingau = Gatinho('Mingau', 'Branco', 5)

#print('O nome do gatinho é:', mingau.nome)
#print('Sua cor é:', mingau.cor)
#print('Sua idade é:', mingau.idade)
#print(mingau.miar())
#print(mingau.andar())
#print(mingau.miar())

print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.velho)
print(mingau.andar())
print(mingau.cansado)