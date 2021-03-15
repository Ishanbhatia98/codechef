from math import log, ceil

two = []
for i in range(27):
    if i == 0:
        two.append(1)
    else:
        two.append(two[i-1]*2)

for _ in range(int(input())):
    c = int(input())
    d = 0
    for i in range(27):
        if two[i] > c:
            d = i
            break
    m = 0
    # need to optimize this part
    for i in range(2**d):
        if c ^ i < 2**d:
            m = max(m, i*(c ^ i))
    print(m)
