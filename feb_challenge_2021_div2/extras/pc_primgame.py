from math import floor
'''
This is the python code for primgame with logic same as the c++ code
but it gives TLE when python is used while AC for c++!!
'''
N = 10**6
primes = [True for _ in range(N+1)]
np = [0 for _ in range(N+1)]
for i in range(2, floor(N**0.5)+1):
    if primes[i]:
        for j in range(i**2, N+1, i):
            primes[j] = False


for i in range(2, N+1):
    np[i] = np[i-1]+primes[i]


for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Divyam' if np[x] > y else 'Chef')
