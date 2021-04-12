for _ in range(int(input())):
    n, m = map(int, input().split())
    l = set(map(int, input().split()))
    if len(l) != m:
        print('Yes')
    else:
        print('No')
