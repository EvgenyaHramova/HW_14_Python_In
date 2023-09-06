import pytest

def fibo_generator(num):
    x, y = 0, 1
    for i in range(num):
        yield y
        x, y = y, x + y

def test_positive():
    assert  fibo_generator(2)

def test_negative():
    with pytest.raises(ValueError):
        fibo_generator(-2), 'Число для вычисления не должно быть отрицательным'

def test_float():
    with pytest.raises(ValueError):
        fibo_generator(0.8), 'Число для вычисления не должно быть вещественным'



if __name__ == '__main__':
    pytest.main()