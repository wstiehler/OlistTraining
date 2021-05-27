
class Produto:
    id_produto = id
    nome = ''
    descricao = ''
    valor = 0.0

    def create(self, nome, descricao, valor):
        self.id_produto = 0
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def read(self):
        return(f"{self.id_produto}-{self.nome}-{self.descricao}-{self.valor} ")

    def update(self):
        pass

    def delete(self):
        pass