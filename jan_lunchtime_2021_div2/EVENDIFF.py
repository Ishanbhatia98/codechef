for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(i%2!=0 for i in l)
    print(min(s, n-s) if s!=n else 0)
