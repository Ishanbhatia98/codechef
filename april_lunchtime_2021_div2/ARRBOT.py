m = 10**9 + 7

n = int(input())
l = list(map(int, input().split()))
s = sum(l)*2
q = int(input())
r = list(map(int, input().split()))
for i in r:
    print(s % m)
    s *= 2
    s %= m
