'''
3-D matrix t[s][size][last]:
    s -> sum of string
    size -> size of string
    last -> last element chosen in the string
'''
t =[[[0 for _ in range(53)] for _ in range(53)] for _ in range(1379)]

#for size = 0 and sum = 0 there exists only one string(empty string)
for i in range(53):
    t[0][0][i]=1

for s in range(1,1379):
    for size in range(1, 53):
        for last in range(1,53):
            #if current element is not chosen
            t[s][size][last]=t[s][size][last-1]
            
            #if current element is chosen its value should not exceed the required sum
            if s-last>=0:
                t[s][size][last]+=t[s-last][size-1][last-1] 
                


for c in range(int(input())):
    n, s= map(int, input().split())
    
    if n>52:
        #Since there are only 52 distinct elements possible
        print(f'Case {c+1}: 0')
    elif s>1378:
        #Since max sum for 52 distinct elements is 1378 -> sum(range(53))
        print(f'Case {c+1}: 0')
    else:
        print(f'Case {c+1}: {t[s][n][-1]}')
