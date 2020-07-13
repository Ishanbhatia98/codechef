for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    x = 0
    for i in range(n-1):
        x += abs(r[i]-r[i+1])

    print(x-n+1)
