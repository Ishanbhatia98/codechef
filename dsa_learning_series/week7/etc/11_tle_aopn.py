#A naive approach to solving the problem
#This problem is a variation of Digit DP
for _ in range(int(input())):
    a = int(input())
    b = int(input())
    count = 0
    for n in range(a+1, b+1):
        s = list(str(n))
        sl, l = -1, -1
        e, o = False, False
        for i in range(len(s)):
            if i>0:
                l = s[i-1]
            if i>1:
                sl = s[i-2]
            if s[i]==l:
                e = 1
            if s[i]==sl:
                o = 1
            if e and o:
                count+=1
                break
    print(count)
        

