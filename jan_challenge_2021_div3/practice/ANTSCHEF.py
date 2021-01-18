'''
Solution from editorial
'''

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    if n==1:
        #Subtask 1
        r = list(map(int, input().split()))
        cp, cn = 0, 0
        for i in range(1, len(r)):
            if r[i]<0:
                cn+=1
            else:
                cp+=1
        print(cp*cn)

    else:
        #Subtask 2
        lines = []
        distances = []
        
        #dictionary to store number of ants at the point both(x and -x)
        d = defaultdict(lambda :0)
        
        for _ in range(n):
            l = list(map(int, input().split()))
            for i in l[1:]:
                d[abs(i)]+=1
                if d[abs(i)]==1:
                    distances.append(abs(i))
                    #distances.add(abs(i))
            lines.append(l[1:])
        total = 0
        for line in lines:
            s = []
            cp, cn = 0, 0
            for e in line:
                if e>0:
                    cp+=1
                    s.append((e, 1))
                else:
                    cn+=1
                    s.append((abs(e), -1))

            s = sorted(s, key=lambda x:x[0])
            for x, y in s:
                #remove the ant thats being currently processed
                if y==-1:
                    cn-=1
                else:
                    cp-=1
                if d[x]>1:
                    #collison changes direction
                    if y==-1:
                        total+=cn
                    else:
                        total+=cp
                else:
                    #collison doesnt change direction
                    if y==1:
                        total+=cn
                    else:
                        total+=cp
        
        #Adding the original collison of ants which meet at the origin at the same time. i.e d[point]>1   
        for point in distances:
            if d[point]>1:
                total+=1
        
        print(total)
