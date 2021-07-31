def f(n, t, k):
    if n == 0:
        return 0
    if k == 0:
        if t+l[n-1] <= s:
            return 1+f(n-1, t+l[n-1], k)
        return 0
    if l[n-1] <= s:
        if t+l[n-1] <= s:
            return max(1+f(n-1, t+l[n-1], k), f(n-1, t, k), 1+f(n-1, l[n-1], k-1))
        else:
            return max(1+f(n-1, l[n-1], k-1), f(n-1, t, k))

    return f(n-1, t, k)


for _ in range(int(input())):
    n, k, s = map(int, input().split())
    l = list(map(int, input().split()))
    print(f(n, 0, k))
