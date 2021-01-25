from math import floor
mn = 10**6+2
primes = [False for _ in range(mn)]
for i in range(2, floor(mn**0.5)+1):
    if primes[i]==False:
        for j in range(i**2, mn, i):
            primes[j] = True
primes[0]= True
primes[1] = True
prefix = [0 for _ in range(mn)]
for i in range(2, mn):
    if primes[i]==False and primes[i-2]==False:
        prefix[i] = 1+prefix[i-1]
    else:
        prefix[i]=prefix[i-1]
for _ in range(int(input())):
    n = int(input())
    if n<=2:
        print(0)
    else:
        print(prefix[n])
