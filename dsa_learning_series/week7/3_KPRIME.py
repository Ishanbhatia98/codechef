#This problem is solved using sieve of eratosthenes

#sieve, primes->stores prime factors of i
primes = [0 for _ in range(1000001)]
for i in range(2, 100001):
    if primes[i]==0:
        for j in range(i, 1000001, i):
            primes[j]+=1

#because for every prime number it has iteself as a prime factor, we add 1
for i in range(2, 1000001):
    if primes[i]==0:
        primes[i]==1

#dp is just a simple 2-D array that computes the the number of numbers with k -prime factors lesser than or equal to n
dp = [[0 for _ in range(6)] for _ in range(1000001)]
for i in range(1000001):
    for j in range(6):
        dp[i][j] = dp[i-1][j]+(primes[i]==j)

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    #we subtract number of K-primes from 0 to b with number of k primes between 0 to a-1,to find the number of k-primes b/w a & b
    print(dp[b][k]-dp[a-1][k])
