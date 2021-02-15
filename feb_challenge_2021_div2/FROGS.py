from math import ceil
'''
Since the maximum value of constraint n(number of frogs is less than 4)
We can use this to our advantage and solv this problem with using brute-force
'''
def q(f, s):

    temp, hops = s, 0
    '''
    tmep<=f
    because we want the frog with the heaviest frog out of the two
    in considetation(f and s)ie frog with w[i]==s, to be placed at a positon which is greater
    than f(strictly greater)
    '''
    while temp<=f:
        temp+=l[s]
        hops+=1
    #adding number of hops needed to place s ahead of f
    total.append(hops)
    return temp

for _ in range(int(input())):
     n = int(input())
     w = list(map(int, input().split()))
     l = list(map(int, input().split()))
     total = []
     f, s, t, fo = 0, 0, 0, 0
     if n==2:
         if w[0]==2:
            r = ceil(2/l[0])
            total.append(r)
     elif n==3:
        f, s, t = w.index(1), w.index(2), w.index(3)
        #checking if pos of s is more than pos of f
        if s<=f:
            #assigning new pos to s
            s = q(f, s)
        #checking if pos of t is more than pos of s
        if t<=s:
            #assigning new pos to t
            t = q(s, t)
     else:
        f, s, t, fo = w.index(1), w.index(2), w.index(3), w.index(4)
        #checking if pos of s is more than pos of f
        if s<=f:
            #assigning new pos to s
            s=q(f, s)
        #checking if pos of t is more than pos of s
        if t<=s:
            #assigning new pos to t
            t=q(s, t)
        #checking if pos of fo is more than pos of t
        if fo<=t:
            #assigning new pos to fo
            fo=q(t, fo)
    
     print(sum(total))
