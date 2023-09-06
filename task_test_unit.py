import unittest
# Создайте функцию генератор чисел Фибоначчи

def fibo_generator(num):
    
    x, y = 0, 1
    for i in range(num):
        yield y
        x, y = y, x + y


class TestFiboGeneratoro(unittest.TestCase):
    def test_negative(self):
        self.assertFalse(fibo_generator(-2), 'Число для вычисления не должно быть отрицательным')

    def test_float(self):
        self.assertError(fibo_generator(0.8), 'Число для вычисления не должно быть вещественным')

    def test_positive(self):
        self.assertTrue(fibo_generator(3))
       
# num = 10
# print(list(fibo_generator(num)))

if __name__ == '__main__':
    unittest.main(verbosity=3)

