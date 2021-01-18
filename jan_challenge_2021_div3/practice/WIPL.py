#Solution from the editorial

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)

    dp = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]

    suf = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        suf[i] = l[i]+suf[i+1]

    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            if j<=l[i]:
                dp[i][j] = l[i]
            elif dp[i+1][j-l[i]]==float('inf'):
                dp[i][j] = float('inf')
            else:
                dp[i][j] = min(dp[i+1][j], l[i]+dp[i+1][j-l[i]])

    f = 1
    for i in range(n-1, -1, -1):
        if suf[i]-dp[i][k]>=k:
            print(n-i)
            f = 0
            break
    
    if f:
        print(-1)
