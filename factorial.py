

def factorial(n:int):
    if n == 0:
        return 1
    return n * factorial(n-1)


def test(func):
    print(func(5))

if __name__ == '__main__':
    test(factorial)