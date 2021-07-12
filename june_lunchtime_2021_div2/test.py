# right '11'
# left ' 1'
# find the ones:
# case if n-1 is also one then take as 0!
# 3 combinations
'''
100
110
101

so for every 101 type you add 1 to res
'''

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in l:
        b = bin(i)[2:]
        if b[len(b)-2] == '1' and b[len(b)-1] == '1':
            ans += 0
        else:
            if b[len(b)-1] == '1':
                ans += 1
    print(ans)
