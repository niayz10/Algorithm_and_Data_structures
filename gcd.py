

def gcd(a, b):
    """ The greatest common divisor. euclidean algorithm"""
    if b == 0:
        return a
    return gcd(b, a%b)

# return a if b == 0 else gcd(b, a%b)

def test(func):
    print(func(10, 12))
    print(func(100, 50))
    print(func(64, 24))

if __name__ == '__main__':
    test(gcd)