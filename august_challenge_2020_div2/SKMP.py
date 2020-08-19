from collections import Counter
import string

def check(p, c, i):
    if c==p[i]:
        return check(p, c, i+1)
    return c<p[i]

def convert(sc):
    sl = ''
    for c in string.ascii_lowercase:
        if c in sc.keys():
            sl+=c*sc[c]
    return sl

for _ in range(int(input())):
    s = input()
    p = input()
    
    sl = convert(Counter(s)-Counter(p))
    
    index = 0
    for i in sl:
        if check(p, i, 0):
            index+=1
    
    print(sl[:index]+p+sl[index:])
