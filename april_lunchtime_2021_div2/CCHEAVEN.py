for _ in range(int(input())):
    n = int(input())
    s = input()
    z, o = 0, 0
    for i in range(n):
        z += (s[i] == '0')
        o += (s[i] == '1')
        if o >= z:
            print('YES')
            break
    else:
        print('NO')
