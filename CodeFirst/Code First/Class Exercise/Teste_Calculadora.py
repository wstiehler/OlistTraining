from unitteste import TestCase

from decimal import Decimal


class Calc:
    def soma(self, x, y):
        if isinstance(x, Decimal) and isinstance(y, Decimal):
            self.cache = x + y
            return self.cache
        elif y is None:
            return x + self.cache
        else:
            raise Exception('Insira somente números')

    def sub(self, x, y):
        if y is None:
            self.cache = x - self.cache
        else:
            self.cache = (x - y)
            return self.cache

    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def clear_cache(self):
        self.cache = 0

class Teste_Calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_soma(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.soma(2, 2), 4)

    def test_soma_neg(self):
        self.assertEqual(self.calc.soma(-2, -3), -5)

    def test_soma_float(self):
        self.assertEqual(self.calc.soma(2.0, 1.0), 3.0)

    def test_sub(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.sub(2, 2), 0)

    def teste_sub_float(self):
        self.assertEqual(self.calc.sub(2.0, 2.0), 0)

    def teste_sub_string(self):
        with self.assertRaises(Exception):
            self.calc.sub('William', 'Villani')

    def test_mult(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.mult(3, 3), 9)

    def teste_div(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.div(3, 3), 1)


