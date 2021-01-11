'''
1.Repeated subtractions(modulus operation) of the array should hint at using the GCD function, to solve this problem.
2.It can be observed that if GCD of two numbers is 1, ie if they are coprime, then the game ends at 1
3.Simlarly for more than two numbers if the GCD for all the numbers is 1, the game will end at 1.
4.For calculating GCD of more than two numbers, it can be proven that GCD(a, b, c)==GCD(GCD(a, b), c)
'''

def gcd(a, b):
    if a==0:
        return b
    if b==0:
        return a
    return gcd(max(a, b)%min(a, b), min(a, b))

def f(n, cgcd):
    if t[n][cgcd]!=-1:
        return t[n][cgcd]
    if n==0:
        '''
        When n is 0, all numbers of the subsequence have been processed if their gcd is 1, then the game ends at 1
        and we return 1, else we return 0
        '''
        if cgcd==1:
            t[n][cgcd] = 1
            return t[n][cgcd]
        t[n][cgcd] = 0
        return t[n][cgcd]
        '''
        For every element(n) in the array, there are two options:
            1.Include it in the subsequence, then cumulative GCD(cgcd) is updated to include the element(at n-1)
            2.Not include it in the subsequence, then cgcd is left as it is.
        Since we have to find total number of subsequences ending at 1, we add 1.+2.
        '''
    t[n][cgcd] = f(n-1, gcd(cgcd, l[n-1]))+f(n-1, cgcd)
    return t[n][cgcd]

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    t = [[-1 for _ in range(max(l)+1)] for _ in range(n+1)]
    
    #Since no element has been processed yet, the cummulative GCd starts at 0.

    ans = f(n, 0)
    print(ans)

