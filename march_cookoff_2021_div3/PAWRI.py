for _ in range(int(input())):
    s = input()
    for i in range(2, len(s)-2):
        if s[i-2]=='p' and s[i-1]=='a' and s[i]=='r' and s[i+1]=='t'  and s[i+2]=='y':
            s = s[:(i)]+'wri'+s[(i+3):]
    print(s)
