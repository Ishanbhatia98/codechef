def f(n):
    if n <= 0:
        return 0
    if n == 1:
        return 20
    if n == 2:
        return 36
    if n == 3:
        return 51
    if n == 4:
        return 60
    '''
    if n == 5:
        return 76
    if n == 6:
        return 88
    if n == 7:
        return 99
    if n == 8:
        return 104
    '''
    r = n//4
    d = n % 4
    return 44*r+f(d)+(4-d)*4


for _ in range(int(input())):
    print(f(int(input())))
