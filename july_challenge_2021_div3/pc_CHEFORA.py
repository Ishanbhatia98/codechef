m = 10**9 + 7

'''
def conv(x):
    if x < 10:
        return x
    s = str(x)
    r = len(s)
    v = s[:(r-1)][::-1]
    s += v
    return int(s)
'''


def conv(a):
    if a < 10:
        return a
    b = a
    a //= 10
    t, c = 0, 1
    while(a % 10 != a):
        t *= 10
        t += (a % 10)
        a //= 10
        c += 1
    t *= 10
    t += a
    b = b*(10**c)
    return (b+t) % m


aa = [0 for _ in range(5005)]
s = [0 for _ in range(5005)]

for i in range(5005):
    aa[i] = conv(i+1)
    if i > 0:
        s[i] = aa[i-1] + s[i-1]


def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


for _ in range(int(input())):
    l, r = map(int, input().split())

    t = 0
    for i in range(l+1, r+1):
        t += aa[i]

    print(power(aa[l-1], s[r]-s[l], m))
