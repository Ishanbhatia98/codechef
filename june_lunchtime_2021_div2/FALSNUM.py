# create list n+1
#func: l[i]*(10**i)
# for i ==0, dont check for x = 0
# prefix sum from n to 0
for _ in range(int(input())):
    a = int(input())
    a = str(a)
    w = ''
    if(a[0] != '1'):
        w = '1' + a
    else:
        w = a[:1] + '0' + a[1:]
    print(int(w))
