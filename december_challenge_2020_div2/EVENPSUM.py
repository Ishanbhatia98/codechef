for _ in range(int(input())):
    a, b = map(int, input().split())
    ea = a//2
    oa = a-ea
    eb = b//2
    ob = b-eb
    print(ea*eb+oa*ob)
