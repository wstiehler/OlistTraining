class Passaro:
    def __init__(self , nome):
        self.nome = nome

class Jogador:
    def __init__(self , camisa):
        self.camisa = camisa

class PicaPau(Passaro):
    def __init__(self , nome , camisa):
        super().__init__(nome)
        self.camisa = camisa

    def __str__(self):
        return f'PicaPau(nome="{self.nome}" , camisa="{self.camisa}")'

    def __repr__(self):
        return f'PicaPau(nome="{self.nome}" , camisa="{self.camisa}")'
