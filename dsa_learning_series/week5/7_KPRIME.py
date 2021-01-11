primes = [0 for _ in range(1000001)]
for i in range(2, 100001):
    if primes[i]==0:
        for j in range(i, 1000001, i):
            primes[j]+=1

for i in range(2, 1000001):
    if primes[i]==0:
        primes[i]==1

dp = [[0 for _ in range(6)] for _ in range(1000001)]
for i in range(1000001):
    for j in range(6):
        dp[i][j] = dp[i-1][j]+(primes[i]==j)

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    print(dp[b][k]-dp[a-1][k])
