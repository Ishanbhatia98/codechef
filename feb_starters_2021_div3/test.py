for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    mx = 0
    for i in range(n-1):
        a, b = l[i+1], l[i]
        m = a*b+max(a-b, b-a)
        mx = max(m, mx)
    print(mx)
