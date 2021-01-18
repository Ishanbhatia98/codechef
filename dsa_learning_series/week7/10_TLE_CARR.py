#This problem gives TLE for even the most efficient code written in python

import numpy as np
mod = 10**9+7

def mo(x):
    return x%mod
def mul(X, Y):
    '''
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mo(mo(X[i][k]) * mo(Y[k][j]))

    return result
    '''
    return np.dot(X, Y)

def f(n, A):
    I = [[1, 0], [0, 1]]

    while(n):
        if n%2:
            I = mul(I, A)
        A = mul(A, A)
        n//=2

    return A


for _ in range(int(input())):
    n, m = map(int, input().split())
    n%=mod
    m%=mod
    
    A = [[m-1, m-1], [1, 0]]
    A = f(n-2, A)
    
    left, right = 0, 0
    left, right = A[1][0]*m*m, A[1][1]*m
    
    ans = mo(left)+mo(right)
    print(ans%mod)
    
