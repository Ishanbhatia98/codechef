#Naive implementation using sive of eratosthenes
#hints were no help, since that is what i already did
#only problem in this code is redundant computations
#logic is completely correct!
from math import floor
for _ in range(int(input())):
    a, b, k = map(int, input().split())
    primes = [0 for _ in range(b+1)]
    
    for i in range(2, b+1):
        if primes[i]==0:
            for j in range(a-(a%i), b+1, i):
                primes[j]+=1
    if k==1:
        for i in range(2, b+1):
            if primes[i]==0:
                primes[i]=1
    c = 0
    for i in range(a, b+1):
        if primes[i]==k:
            c+=1
    print(c)
    
