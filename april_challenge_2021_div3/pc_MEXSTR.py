from collections import defaultdict as dd


def issubseq(a, b):
    if d[a, b] != -1:
        return d[a, b]
    j = 0
    for i in range(len(b)):
        if a[j] == b[i]:
            j += 1
        if j == len(a):
            d[a, b] = 1
            return 1
    d[a, b] = 0
    return 0


def generate_binary(s):
    if '0' not in s:
        return '0'
    q = []
    q.append('1')
    while True:
        s1 = q[0]
        q.remove(q[0])
        if not issubseq(s1, s):
            return s1
        s2 = s1
        q.append(s1+'0')
        q.append(s2+'1')


for _ in range(int(input())):
    s = input()
    d = dd(lambda: -1)
    print(generate_binary(s))
