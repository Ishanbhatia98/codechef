from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    r = [0 for _ in range(31)]
    for i in l:
        b = bin(i)[2:]

        for j in range(len(b)):
            z = 31+j-len(b)
            if b[j] == '1':
                r[z] += 1
    ans = 0
    for i in r:
        ans += ceil(i/k)
    print(ans)
