# Создайте функцию генератор чисел Фибоначчи

def fibo_generator(num):
    """
    >>> fibo_generator(-1)
    False
    >>> fibo_generator(0.5)
    False
    """


    x, y = 0, 1
    for i in range(num):
        yield y
        x, y = y, x + y
       
# num = 10
# print(list(fibo_generator(num)))



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
