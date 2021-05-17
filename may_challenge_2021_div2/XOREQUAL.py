m = 10**9 + 7
d = [1 for _ in range(10**5 + 1)]
for i in range(2, 10**5 + 1):
    d[i] = (d[i-1]*2) % m
for _ in range(int(input())):
    n = int(input())
    print(d[n] % m)
