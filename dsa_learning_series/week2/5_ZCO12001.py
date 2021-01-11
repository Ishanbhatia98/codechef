in = int(input())
s = list(map(int, input().split()))

stack = 0
nesting_d = 0
nesting_p = 1

max_l = 0
len_p = 1
previous = 0
for i in range(n):
    if s[i]==1:
        stack+=1
    else:
        if stack>nesting_d:
            nesting_d = stack
            nesting_p = i
        stack-=1
    if stack==0:
        l = i-previous+1
        if l>max_l:
            max_l = l
            len_p = previous
        previous = i+1

print(nesting_d, nesting_p, max_l, len_p+1)
