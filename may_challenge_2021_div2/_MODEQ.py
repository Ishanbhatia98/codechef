for _ in range(int(input())):
    n, m = map(int, input().split())
    v = [1 for _ in range(n+1)]
    a = 0
    for i in range(2, n+1):
        r = m % i
        a += v[r]
        for j in range(r, n+1, i):
            v[j] += 1
    print(a)
