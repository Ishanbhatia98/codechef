for _ in range(int(input())):
    n, k, d = map(int, input().split())
    l = list(map(int, input().split()))
    print(min(sum(l)//k, d)) 
