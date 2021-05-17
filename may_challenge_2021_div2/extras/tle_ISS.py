n = 4*10**6 + 5
phi = [i for i in range(n)]
ans = [0 for _ in range(n)]
for p in range(2, n):
    if phi[p] == p:
        phi[p] = p-1
        for i in range(2*p, n, p):
            phi[i] = (phi[i]//p)*(p-1)


for i in range(1, n):
    ans[i] += i-1
    for j in range(2*i, n, i):
        ans[j] += i*((1+phi[j//i])//2)

for _ in range(int(input())):
    print(ans[4*(int(input()))+1])
