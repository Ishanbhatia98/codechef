for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sa, sb = sum(a), sum(b)
    if sa>sb:
        print(0)
    else:
        a = sorted(a)
        b = sorted(b, reverse=True)
        c = 0
        for i in range(min(n, m)):
            sa = sa + b[i] - a[i]
            sb = sb + a[i] - b[i]
            c+=1
            if sa>sb:
                print(c)
                break

        if sb>=sa:
            print(-1)
