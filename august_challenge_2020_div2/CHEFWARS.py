def check(h, p):
    if h<=0:
        return 1
    elif p<=0:
        return 0
    else:
        return check(h-p, p//2)

for _ in range(int(input())):
    h, p = map(int, input().split())
    print(check(h, p))
