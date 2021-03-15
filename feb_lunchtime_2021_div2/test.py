from collections import Counter
for _ in range(int(input())):
    s = input()
    o, mo = 0, 0
    c = Counter(list(s))
    for v in c.values():
        if v%2==0:
                mo+=1
        elif v==1:
            o+=1
    if mo<o:
        print('NO')
    else:
        print('YES')
