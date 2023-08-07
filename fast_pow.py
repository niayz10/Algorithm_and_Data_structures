

def fast_pow(a:float, n:int):
    """The fast pow algorithm"""
    if n == 0:
        return 1
    elif n % 2 != 0: # for odd numbers
        return a * fast_pow(a, n - 1)
    return fast_pow(a**2, n // 2) # for even numbers


def test(func):
    print(func(2, 10)) # 1024

if __name__ == '__main__':
    test(fast_pow)