for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    ans = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            ff, fs = s[i][0], s[i][1:]
            sf, ss = s[j][0], s[j][1:]
            if ff+ss not in s and sf+fs not in s:
                ans+=1
    print(2*ans)
