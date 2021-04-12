for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = set()
    for i in range(n):
        for j in range(1, l[i]+1):
            x, y = j, i+1
            m = min(x, y)
            if m == 1:
                s.add((x, y))
            else:
                m -= 1
                s.add((x-m, y-m))
    print(s)
    print(len(s))
