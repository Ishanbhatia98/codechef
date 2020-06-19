def p(n, count):
    if n==1:
        return count
    elif n%2!=0:
        return count
    else:
        return p(n//2, count+1)


for _ in range(int(input())):
    n = int(input())
    c = p(n, 0)
    print(n//(2**(c+1)))
