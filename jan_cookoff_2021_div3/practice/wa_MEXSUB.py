'''
This code gives WA verdict on cc.
Tried to solve this problem as a variation of the "Matrix Chain Multiplication" problem using DP.
There is a minor error in this code which I have failed to detect; upon detection this code should work!
'''
def mex(a):
    if len(a)==0:
        return 0
    for i in range(max(a)+1):
        if i not in a:
            return i
def f(i, j):
    if i>=j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    ans = 0
    for k in range(i+1, j):
        if i!=k and k!=j:
            if mex(a[i:k])==mex(a[k:j]):
                if dp[i][k]==-1:
                    left = f(i, k)
                else:
                    left = dp[i][k]
                
                if dp[k][j]==-1:
                    right = f(k, j)
                else:
                    right = dp[k][j]

                ans+= 1 + left + right
    
    dp[i][j] = ans
    return ans
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    print(f(0, n))
    
    

