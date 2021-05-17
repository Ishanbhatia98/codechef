def check(a, b):
    return (b * (m//b) % a) == 0


for _ in range(int(input())):
    n, m = map(int, input().split())
    t = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            t += (j % i == 0) or (i*(j+1) > m and i*j <= m)
    print(t)
