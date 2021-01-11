for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    gm, cm = 0, 0
    m = 19**9
    for i in range(n):
        #cm = max(l[i]+cm, l[i])
        if l[i]>cm+l[i]:
            m = 10**9
            cm = l[i]
        else:
            m = min(m, l[i])
            cm+=l[i]
        gm = max(gm, cm)
    if gm==0:
        if 0 in l:
            print(gm)
        else:
            print(max(l))
    else:
        if m==10**9:
            print(gm)
        else:
            if m<0:
                print(gm-m)
            else:
                print(gm)
