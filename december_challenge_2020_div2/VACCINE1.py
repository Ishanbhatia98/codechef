d1, v1, d2, v2, p = map(int, input().split())
d = 1
t = 0
while True:
    if d>=d1:
        t+=v1
    if d>=d2:
        t+=v2
    #print(f'Day:{d}. total:{t}')
    if t>=p:
        break
    d+=1
print(d)
