for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    '''
    Objective is to choose three numbers such that the difference of their sums is maximum!
    Choosing f(first) as minimum element of l
    Choosing t(third) as maximum element of l
    For choosing s(second) we iterate through index 1 to n-2(because we have already chosen 
    elements at index 1 and n-1) and choose the maximum such value that fits our condition 
    i.e
    choose maximum of abs(f-s)+abs(s-t)+abs(t-f), iterating through all values of s ->[1, n-2]
    '''
    f, t = l[0], l[n-1]
    m = 0
    for s in l[1:n-1]:
        m = max(m,abs(f-s)+abs(s-t)+abs(f-t))
    print(m)
