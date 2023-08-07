

def move(n:int, start:int, finish:int):
    if n == 1:
        print(f'n = {n} start = {start} finish = {finish}')
    else:
        tmp = 6 - start - finish
        move(n - 1, start, tmp)
        print(f'n = {n} start = {start} finish = {finish}')
        move(n - 1, tmp, finish)

def test(func):
    func(3, 1, 3)


if __name__ == '__main__':
    test(move)