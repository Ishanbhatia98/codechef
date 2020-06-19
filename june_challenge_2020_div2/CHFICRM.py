for _ in range(int(input())):
    n = int(input())
    coins = [0, 0, 0]
    l = list(map(int, input().split()))
    f = 1
    for coin in l:
        change = coin - 5
        if coin==5:
            coins[0]+=1
        elif coin==10:
            coins[1]+=1
        else:
            coins[2]+=1

        if change==0:
            continue
        elif change==5 and coins[0]>0:
            coins[0]-=1
        elif change==10 and coins[1]>0:
            coins[1]-=1
        elif change==15 and coins[2]>0:
            coint[2]-=1
        else:
            f = 0


    if f:
        print('YES')
    else:
        print('NO')
