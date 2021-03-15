for _ in range(int(input())):
    n = int(input())
    c = bin(n)[2:]
    a, b = '', ''
    for i in range(len(c)):
        if i == 0:
            a += '1'
            b += '0'
        else:
            if c[i] == '1':
                a += '0'
                b += '1'
            else:
                a += '1'
                b += '1'
    a, b = int(a, 2), int(b, 2)
    print(a*b)
