class nome_da_class:
    def __init__(self, argument_1, argument_2, argument_3):
        self.attribute_1 = argument_1
        self.attribute_2 = argument_2
        self.attribute_3 = argument_3

    def _private(self, valor):
        pass

    def method_1(self):
        return self._private(self.attribute_1)

    def method_2(self, valor):
        return self.attribute_2 * valor


xerox = nome_da_class('paper', 'ink', 'toner')
