'''
#recursive approach
def f(n):
    #if n is less than 2 input becomes invalid
    if n<2:
        return 0
    #if n==2 then point scored is by cannonshot, if n==3 point socred is by in-off
    #i.e. there is only one way!
    if n==2 or n==3:
        return 1
    #memoization
    if t[n]!=-1:
        return t[n]
    #decision tree
    if(n-3>=2):
        #if n>=5 each point scored can either be 2(cannon shot) or 3(in-off)
        t[n] = (f(n-2)+f(n-3))%mod
    elif(n-2>=2):
        #this condition exists only for n==4
        t[n] = f(n-2)%mod
    return t[n]
'''
#m->maximum value of score for input
m = 10**6 +1
mod = 10**9 + 9

#bottom up approach
dp = [0 for _ in range(m)]

#i==2 and i==3 are base conditions
dp[2] = 1
dp[3] = 1

for i in range(4, m):
    dp[i] = (dp[i-2]+dp[i-3])%mod

for _ in range(int(input())):
    print(dp[int(input())])

