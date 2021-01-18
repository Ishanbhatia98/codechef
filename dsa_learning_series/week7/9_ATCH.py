for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    #if all are negative integers
    if all(i<=0 for i in l):
        print(max(l))

    #if all are postive integers
    elif all(i>0 for i in l):
        print(sum(l))
    else:
        gm, cm, m = -float('inf'), 0, float('inf')
        for i in range(n):
            
            cm+=l[i]

            #gm(global maximum) stores the largest subarray
            gm = max(gm, cm, cm-m)
            
            #m(minimum) stores the smallest element of the subarray
            m = min(m, l[i])

            #if cm(current maximum) is less than zero then new subarray is started
            if cm<0:
                #current maximum is reset to zero
                cm = 0
                #minimum is reset to infinity
                m = float('inf')

        print(gm)
        
