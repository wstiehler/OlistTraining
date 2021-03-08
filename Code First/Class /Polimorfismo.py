class Pizza:
    pedaços = 8

    @classmethod
    def mudar_tamanho(cls , pedaços):
        cls.pedaços = pedaços

    @staticmethod
    def ingredientes():
        return 'ingredientes'


class Mussarela(Pizza):

    @staticmethod
    def ingredientes():
        return ['queijo' ,
                'azeitona' ,
                'trigo']
