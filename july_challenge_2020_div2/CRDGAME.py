def convert(x):
    return sum(list(map(int,  list(str(x)))))

for _ in range(int(input())):
    n = int(input())
    a_n, b_n = 0, 0
    for _ in range(n):
        a, b = map(int, input().split())
        a, b = convert(a), convert(b)
        if a>b:
            a_n+=1
        elif b>a:
            b_n+=1
        else:
            a_n+=1
            b_n+=1
    if a_n==b_n:
        print(2, a_n)
    elif a_n>b_n:
        print(0, a_n)
    else:
        print(1, b_n)

