for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    total = 0
    m = 10**9
    for i in l:
        m = min(m, i)

        total += m
    print(total)
