import string
s = string.ascii_lowercase
d = dict()
for i in range(0, 16):
    b = bin(i)[2:]
    if len(b)!=4:
        z = '0'*(4-len(b))
        d[z+b] =  s[i]
    else:
        d[b]= s[i]
for _ in range(int(input())):
    n = int(input())
    l = input()
    for i in range(0, n, 4):
        print(d[l[i:i+4]], end='')
    print()
