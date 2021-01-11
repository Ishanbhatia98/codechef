def convert(l):
    for i in range(n-1):
        if l[i] & l[i+1] ==0:
            l[i], l[i+1] = l[i+1], l[i]
    for i in range(1, n-1):
        if l[i] & l[i+1]==0:
            l[i], l[i+1] = l[i+1], l[i]
    return l
def check(l):
    for i in range(n-1):
        if l[i] & l[i+1]==0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    l = list(range(1, n+1))
    l = convert(l)

    if check(l):
        print(*l)
    else:
        l = convert(l)
        if check(l):
            print(*l)
        else:
            print(-1)



