#solution from editorial

for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]
    if n%2==0 or m%2==0:
        '''
        if n*m was even then there are two arrangements to have maximum islands.
        
        we can place land(*) on odd parity positions i.e (i+j)%2!=0
        and we can place water(.) on even parity posiions i.e (i+j)%2==0
        count2 counts the conversions needed for this arrangement

        OR
        
        we can place water(.) on odd parity positions i.e (i+j)%2!=0
        and we can place land(*) on even parity posiions i.e (i+j)%2==0
        count1 counts the conversions needed for this arrangement1
        
        count1 -> '*' - even
                  '.' - odd

        count1 -> '*' - odd
                  '.' - even
        '''
        count1, count2 = 0, 0
        for i in range(n):
            for j in range(m):
                if (i+j)%2==0:
                    if matrix[i][j]!='*':
                        count1+=1
                    if matrix[i][j]!='.':
                        count2+=1
                else:
                    if matrix[i][j]!='*':
                        count2+=1
                    if matrix[i][j]!='.':
                        count1+=1
        print(min(count1, count2))
    else:
        '''
        if n*m was odd then there is only one type of arrangement to have maximum islands.
        since even parity positions will be 1 more than odd parity positions i.e
        
        Number of even parity positions -> ceil(n*m/2)
        Number of odd parity positions -> floor(n*m/2)
        
        Thus the only arrangemnt will be to place land(*) on even parity positions i.e (i+j)%2==0
        and place water(.) on odd parity positions i.e. (i+j)%2!=0
        count counts the conversions needed for this arrangement

        count -> '*' - even
                 '.' - odd
        '''
        count = 0
        for i in range(n):
            for j in range(m):
                if (i+j)%2==0:
                    if matrix[i][j]!='*':
                        count+=1
                else:
                    if matrix[i][j]!='.':
                        count+=1

        print(count)
