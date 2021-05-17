for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    x, o = False, False

    if a[0] == a[1] == a[2]:
        x |= (a[0] == 'X')
        o |= (a[0] == 'O')

    if b[0] == b[1] == b[2]:
        x |= (b[0] == 'X')
        o |= (b[0] == 'O')

    if c[0] == c[1] == c[2]:
        x |= (c[0] == 'X')
        o |= (c[0] == 'O')

    if a[0] == b[0] == c[0]:
        x |= (a[0] == 'X')
        o |= (a[0] == 'O')

    if a[1] == b[1] == c[1]:
        x |= (a[1] == 'X')
        o |= (a[1] == 'O')

    if a[2] == b[2] == c[2]:
        x |= (a[2] == 'X')
        o |= (a[2] == 'O')

    if a[0] == b[1] == c[2]:
        x |= (a[0] == 'X')
        o |= (a[0] == 'O')

    if c[0] == b[1] == a[2]:
        x |= (c[0] == 'X')
        o |= (c[0] == 'O')

    nx = a.count('X')+b.count('X')+c.count('X')
    no = a.count('O')+b.count('O')+c.count('O')
    nz = a.count('_')+b.count('_')+c.count('_')

    if nx-no > 1 or no > nx:
        print(3)
    elif x and o:
        print(3)
    elif x and not o:

        if nx-no == 1:
            print(1)
        else:
            print(3)

    elif o and not x:

        if nx == no:
            print(1)
        else:
            print(3)

    else:

        if nz > 0:
            print(2)
        else:
            print(1)
