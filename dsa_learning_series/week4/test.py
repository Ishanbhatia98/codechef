def f(l, r):
    if l > r:
        return 0

    m = l+(r-l)//2
    t = 0

    for i in range(l, m+1):
        for j in range(m, r+1):
            if i != j:
                t += (s[i] > s[j])
    return t+f(l, m-1)+f(m+1, r)


n = int(input())
s = list(map(int, input().split()))
print(f(0, n-1))
