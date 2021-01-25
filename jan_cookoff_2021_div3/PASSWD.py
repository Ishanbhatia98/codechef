import string

def checkl(s):
    for i in s:
        if i in string.ascii_lowercase:
            return True
    return False

def checku(s):
    for i in s[1:n-1]:
        if i in string.ascii_uppercase:
            return True
    return False

def checkd(s):
    for i in s[1:n-1]:
        if i in list(map(str, list(range(10)))):
            return True
    return False
def checks(s):
    for i in s[1:n-1]:
        if i in ['@', '#', '%', '&', '?']:
            return True
    return False



for _ in range(int(input())):
    s = list(input())
    n = len(s)
    if n>=10 and checkl(s) and checku(s) and checkd(s) and checks(s):
        print('YES')
    else:
        print('NO')
