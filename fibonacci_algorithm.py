import sys

def fibonacci(n:int):
    """The fibonacci algorithm"""
   
    if n == 0:        
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n - 2) + fibonacci(n - 1)

def test_fibonacci_algorithm(func):
    print(f'Test the {func.__doc__}')

    n = int(input())
    
    print(func(n))

test_fibonacci_algorithm(fibonacci)