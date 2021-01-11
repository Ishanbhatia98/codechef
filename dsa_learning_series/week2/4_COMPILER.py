for _ in range(int(input())):
    s = input()
    status = 0
    a = ans = 0
    for i in range(len(s)):
        if s[i] == '<':
            a += 1
        else:
            a -= 1
        if a < 0:
            break
        if a == 0:
            ans = max(ans, i+1)
    print(ans)
