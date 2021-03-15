for _ in range(int(input())):
    s = list(map(int, list(input())))
    c = s[0]
    for i in range(1, len(s)):
        if s[i] == 1:
            if s[i-1] != 1:
                c += 1
    print(c)
