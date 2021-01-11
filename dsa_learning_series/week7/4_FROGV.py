#The solution to this problem is unavailible in the live-sessions.
#This problem is solved using 1-D Dynamic Programming
n, k, p = map(int, input().split())
l = list(enumerate(list(map(int, input().split())), 1))
l = sorted(l, key=lambda x:x[1])

f = 0
dp = {l[0][0]:f}
for i in range(1, n):
    '''
    1.If the difference is lesser than or equal to k, then the farthest element(frog) to the left remains the same.
    2.If the difference is greater than k, then the farthest element reacheable is increased by 1 index since, elements(frogs) before that index are now
      unreachable

    '''
    if l[i][1]-l[i-1][1]<=k:
        dp[l[i][0]]=f
    else:
        f+=1
        dp[l[i][0]]=f

for _ in range(p):
    a, b = map(int, input().split())
    '''
    If the Farthest element(frog) reachable to the left is same for the two elements(frogs), then they can communicate, else they cannot.
    '''
    if dp[a]==dp[b]:
        print('Yes')
    else:
        print('No')
