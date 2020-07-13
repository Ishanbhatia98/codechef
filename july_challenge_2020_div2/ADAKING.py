for _ in range(int(input())):
    k = int(input())
    if k<=8:
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
        print('X'*8)
        for _ in range(6):
            print('.'*8)
    elif k<=16:
        print('.'*8)
        k = k-8
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
        print('X'*8)
        for _ in range(5):
            print('.'*8)
    elif k<=24:
        for _ in range(2):
            print('.'*8)
        k = k-16
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
        print('X'*8)
        for _ in range(4):
            print('.'*8)
    elif k<=32:
        for _ in range(3):
            print('.'*8)
        k = k-24
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
        print('X'*8)
        for _ in range(3):
            print('.'*8)
    elif k<=40:
        for _ in range(4):
            print('.'*8)
        k = k-32
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
        print('X'*8)
        for _ in range(2):
            print('.'*8)
    elif k<=48:
        for _ in range(5):
            print('.'*8)
        k = k-40
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
        print('X'*8)
        print('.'*8)
    elif k<=56:
        for _ in range(6):
            print('.'*8)
        k=k-48
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
        print('X'*8)
    else:
        for _ in range(7):
            print('.'*8)
        k=k-56
        s = 'O'+'.'*(k-1)+'X'*(8-k)
        print(s)
