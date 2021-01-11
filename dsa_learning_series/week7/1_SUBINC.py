#longest increasing subsequence and kadanes algorithm is a pre-requisite to solve this problem

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    dp = [1 for _ in range(n)]

    #res->to store max length of LIS on every iteration
    res = 0

    for i in range(1, n):
        '''
        #code for LIS
        for j in range(i):
            if dp[i]>dp[j]:
                dp[i] = max(1+dp[j], dp[i])
        res = max(dp[i], res)
        '''
        #ith element has to be greater than or equal to i-1
        if l[i]>=l[i-1]:
            dp[i] = max(dp[i], 1+dp[i-1])
        
    #print(res)
    print(sum(dp))
    
