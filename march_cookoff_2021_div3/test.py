for _ in range(int(input())):
    n, m, k = map(int, input().split())
    A = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            A[i][j] = k+i+j+2

    print(A[0][0], A[1][1] ,A[1][2], A[0][0]^A[1][1]^A[1][2]^A[0][1])
