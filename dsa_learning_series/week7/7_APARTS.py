#The solution to this problem is unavailble in the live session
#This problemm can be solved using the hints provided

from copy import deepcopy as dc

for _ in range(int(input())):
    n, m = map(int, input().split())
    #Taking matrix A as input
    a = [list(map(int, input().split())) for _ in range(n)]
    
    #copying matrix a to dp
    dp = dc(a)

    for i in range(n):
        for j in range(m):
            #If a[i][j] is greater than or equal to dp, then it is washed after it gets dirty for the last time
            print(int(a[i][j]>=dp[i][j]) , end='')
            '''
            since for every window at location (i, j)
            Three windows get dirty cleaning it which are located at(when seen from the top floor ie i==n-1):
            1.(i+1, j-1), 2.(i+1, j) and 3.(i+1, j+1)
            So we update the last time each of these windows gets washed and we choose between the current time proposed and 
            the time already alotted to the window at the location.we choose the maximum of the availible choices.
            '''
            for k in [-1,0,1]:
                if i+1 < n and 0 <= j+k < m:
                    dp[i+1][j+k] = max(dp[i+1][j+k], dp[i][j])
        print()
